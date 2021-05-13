.DEFAULT_GOAL:=help
SHELL:=/bin/bash

define run_docker
	$(if $(1), echo $(1), echo 'services list is not defined'; exit 1)
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up "$1"
endef

define rebuild_docker
	$(if $(1), echo $(1), echo 'services list is not defined'; exit 1)
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build "$1"
endef

define build_docker
	$(if $(1), echo $(1), echo 'services list is not defined'; exit 1)
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build "$1"
	docker-compose push "$1"
endef

define run_ansible
	$(if $(1), echo Using playbook $(1), echo 'playbook is not defined'; exit 1)
	ANSIBLE_CONFIG=infrastructure/ansible.cfg ansible-playbook -i infrastructure/inventory.ini infrastructure/$1
endef

all: help

run-services:  ## Run related services
	@$(call run_docker,"db")

build-want:  ## Build and push detalkin
	@$(call build_docker,"want")

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

run-db: ## Run db without app
	@$(call run_docker,"db")
