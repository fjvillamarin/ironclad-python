# UpdateWorkflowMetadata200ResponseSchemaLineItemsElementType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**var_schema** | [**UpdateWorkflowMetadata200ResponseSchemaLineItemsElementTypeSchema**](UpdateWorkflowMetadata200ResponseSchemaLineItemsElementTypeSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_workflow_metadata200_response_schema_line_items_element_type import UpdateWorkflowMetadata200ResponseSchemaLineItemsElementType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowMetadata200ResponseSchemaLineItemsElementType from a JSON string
update_workflow_metadata200_response_schema_line_items_element_type_instance = UpdateWorkflowMetadata200ResponseSchemaLineItemsElementType.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowMetadata200ResponseSchemaLineItemsElementType.to_json())

# convert the object into a dict
update_workflow_metadata200_response_schema_line_items_element_type_dict = update_workflow_metadata200_response_schema_line_items_element_type_instance.to_dict()
# create an instance of UpdateWorkflowMetadata200ResponseSchemaLineItemsElementType from a dict
update_workflow_metadata200_response_schema_line_items_element_type_from_dict = UpdateWorkflowMetadata200ResponseSchemaLineItemsElementType.from_dict(update_workflow_metadata200_response_schema_line_items_element_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


