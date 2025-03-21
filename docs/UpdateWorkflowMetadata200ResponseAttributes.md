# UpdateWorkflowMetadata200ResponseAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_name** | **str** |  | [optional] 
**amount** | **int** |  | [optional] [default to 0]
**fee** | [**UpdateWorkflowMetadata200ResponseAttributesFee**](UpdateWorkflowMetadata200ResponseAttributesFee.md) |  | [optional] 
**draft** | [**List[UpdateWorkflowMetadata200ResponseAttributesDraftInner]**](UpdateWorkflowMetadata200ResponseAttributesDraftInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_workflow_metadata200_response_attributes import UpdateWorkflowMetadata200ResponseAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowMetadata200ResponseAttributes from a JSON string
update_workflow_metadata200_response_attributes_instance = UpdateWorkflowMetadata200ResponseAttributes.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowMetadata200ResponseAttributes.to_json())

# convert the object into a dict
update_workflow_metadata200_response_attributes_dict = update_workflow_metadata200_response_attributes_instance.to_dict()
# create an instance of UpdateWorkflowMetadata200ResponseAttributes from a dict
update_workflow_metadata200_response_attributes_from_dict = UpdateWorkflowMetadata200ResponseAttributes.from_dict(update_workflow_metadata200_response_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


