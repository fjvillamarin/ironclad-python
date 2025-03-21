# WorkflowResponseModelAttributesDraftInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**version_number** | **float** |  | [optional] 
**filename** | **str** |  | [optional] 
**download** | **str** |  | [optional] 
**last_modified** | [**WorkflowResponseModelAttributesDraftInnerLastModified**](WorkflowResponseModelAttributesDraftInnerLastModified.md) |  | [optional] 

## Example

```python
from openapi_client.models.workflow_response_model_attributes_draft_inner import WorkflowResponseModelAttributesDraftInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResponseModelAttributesDraftInner from a JSON string
workflow_response_model_attributes_draft_inner_instance = WorkflowResponseModelAttributesDraftInner.from_json(json)
# print the JSON string representation of the object
print(WorkflowResponseModelAttributesDraftInner.to_json())

# convert the object into a dict
workflow_response_model_attributes_draft_inner_dict = workflow_response_model_attributes_draft_inner_instance.to_dict()
# create an instance of WorkflowResponseModelAttributesDraftInner from a dict
workflow_response_model_attributes_draft_inner_from_dict = WorkflowResponseModelAttributesDraftInner.from_dict(workflow_response_model_attributes_draft_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


