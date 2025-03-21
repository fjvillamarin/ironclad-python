# WorkflowResponseModelAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_name** | **str** |  | [optional] 
**amount** | **int** |  | [optional] [default to 0]
**fee** | [**UpdateWorkflowMetadata200ResponseAttributesFee**](UpdateWorkflowMetadata200ResponseAttributesFee.md) |  | [optional] 
**draft** | [**List[WorkflowResponseModelAttributesDraftInner]**](WorkflowResponseModelAttributesDraftInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.workflow_response_model_attributes import WorkflowResponseModelAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResponseModelAttributes from a JSON string
workflow_response_model_attributes_instance = WorkflowResponseModelAttributes.from_json(json)
# print the JSON string representation of the object
print(WorkflowResponseModelAttributes.to_json())

# convert the object into a dict
workflow_response_model_attributes_dict = workflow_response_model_attributes_instance.to_dict()
# create an instance of WorkflowResponseModelAttributes from a dict
workflow_response_model_attributes_from_dict = WorkflowResponseModelAttributes.from_dict(workflow_response_model_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


