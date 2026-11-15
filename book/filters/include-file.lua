-- include-file.lua: replace a code block's body with the contents of a file.
-- Usage: ```{.yaml include="path/to/file" start-line=2 end-line=5}
-- Paths resolve against the book project dir (book/), since Quarto merges
-- chapters into one document. A missing file is a hard build error.

local function dirname(p)
  return (p:match("^(.*)/[^/]*$")) or "."
end

local function read_file(path)
  local fh = io.open(path, "r")
  if not fh then return nil end
  local content = fh:read("a")
  fh:close()
  return content
end

local function resolve(path)
  local candidates = {}
  if path:sub(1, 1) == "/" then
    table.insert(candidates, path)
  else
    -- Project dir first: the input file differs per format (chapter vs merged book).
    local proj = (quarto and quarto.project and quarto.project.directory)
      or os.getenv("QUARTO_PROJECT_DIR")
    if proj then table.insert(candidates, proj .. "/" .. path) end
    table.insert(candidates, path)
  else
    -- Quarto renders from a temp copy, so prefer its record of the real source file.
    if quarto and quarto.doc and quarto.doc.input_file then
      table.insert(candidates, dirname(quarto.doc.input_file) .. "/" .. path)
    end
    local inputs = PANDOC_STATE and PANDOC_STATE.input_files
    if inputs and inputs[1] then
      table.insert(candidates, dirname(inputs[1]) .. "/" .. path)
    end
    table.insert(candidates, path)
  end
  for _, c in ipairs(candidates) do
    local content = read_file(c)
    if content then return content end
  end
  error("include-file: cannot read '" .. path .. "' (tried: " ..
        table.concat(candidates, ", ") .. ")")
end

function CodeBlock(cb)
  local path = cb.attributes["include"]
  if not path then return nil end
  local content = resolve(path)
  local first = tonumber(cb.attributes["start-line"])
  local last = tonumber(cb.attributes["end-line"])
  if first or last then
    local lines = {}
    for line in (content .. "\n"):gmatch("(.-)\n") do
      table.insert(lines, line)
    end
    if lines[#lines] == "" then table.remove(lines) end
    local selected = {}
    for i = first or 1, last or #lines do
      if lines[i] then table.insert(selected, lines[i]) end
    end
    content = table.concat(selected, "\n")
  end
  content = content:gsub("\n$", "")
  cb.text = content
  cb.attributes["include"] = nil
  cb.attributes["start-line"] = nil
  cb.attributes["end-line"] = nil
  return cb
end
