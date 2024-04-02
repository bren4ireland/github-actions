provider "azurerm" {
    features {}
}

resource "azurerm_resource_group" "example" {
    name     = "brens-resource-group"
    location = "west US"
}