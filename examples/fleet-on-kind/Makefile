CLUSTER := fleet-on-kind
CONFIG  := kind-config.yaml

.PHONY: up down smoke

up:
	@if kind get clusters 2>/dev/null | grep -qx '$(CLUSTER)'; then \
		echo "cluster $(CLUSTER) already exists"; \
	else \
		kind create cluster --config $(CONFIG); \
	fi

down:
	@if kind get clusters 2>/dev/null | grep -qx '$(CLUSTER)'; then \
		kind delete cluster --name $(CLUSTER); \
	else \
		echo "cluster $(CLUSTER) not present"; \
	fi

smoke:
	@rc=0; \
	$(MAKE) up && kubectl --context kind-$(CLUSTER) wait --for=condition=Ready node --all --timeout=120s || rc=$$?; \
	$(MAKE) down; \
	exit $$rc
