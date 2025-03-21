# UpdateWorkflowMetadata200ResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_name** | [**UpdateWorkflowMetadata200ResponseSchemaCounterpartyName**](UpdateWorkflowMetadata200ResponseSchemaCounterpartyName.md) |  | [optional] 
**amount** | [**UpdateWorkflowMetadata200ResponseSchemaAmount**](UpdateWorkflowMetadata200ResponseSchemaAmount.md) |  | [optional] 
**fee** | [**UpdateWorkflowMetadata200ResponseSchemaFee**](UpdateWorkflowMetadata200ResponseSchemaFee.md) |  | [optional] 
**draft** | [**UpdateWorkflowMetadata200ResponseSchemaDraft**](UpdateWorkflowMetadata200ResponseSchemaDraft.md) |  | [optional] 
**line_items** | [**UpdateWorkflowMetadata200ResponseSchemaLineItems**](UpdateWorkflowMetadata200ResponseSchemaLineItems.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_workflow_metadata200_response_schema import UpdateWorkflowMetadata200ResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowMetadata200ResponseSchema from a JSON string
update_workflow_metadata200_response_schema_instance = UpdateWorkflowMetadata200ResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowMetadata200ResponseSchema.to_json())

# convert the object into a dict
update_workflow_metadata200_response_schema_dict = update_workflow_metadata200_response_schema_instance.to_dict()
# create an instance of UpdateWorkflowMetadata200ResponseSchema from a dict
update_workflow_metadata200_response_schema_from_dict = UpdateWorkflowMetadata200ResponseSchema.from_dict(update_workflow_metadata200_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


