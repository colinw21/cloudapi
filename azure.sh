#!/bin/bash

#az account list
#az account set -s PAYG-DevOps
#az rest -m get -u 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/gwengroup/providers/Microsoft.Network/networkVirtualApplianceSKUs?api-version=2020-05-01'
az rest -m get -u 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/gwengroup/providers/Microsoft.Network/virtualHubs/gwenhub?api-version=2020-05-01'
