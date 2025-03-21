# WorkflowResponseModelCreator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | 
**email** | **str** |  | 
**title** | **str** |  | 
**username** | **str** |  | 
**metadata** | **object** |  | 

## Example

```python
from openapi_client.models.workflow_response_model_creator import WorkflowResponseModelCreator

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResponseModelCreator from a JSON string
workflow_response_model_creator_instance = WorkflowResponseModelCreator.from_json(json)
# print the JSON string representation of the object
print(WorkflowResponseModelCreator.to_json())

# convert the object into a dict
workflow_response_model_creator_dict = workflow_response_model_creator_instance.to_dict()
# create an instance of WorkflowResponseModelCreator from a dict
workflow_response_model_creator_from_dict = WorkflowResponseModelCreator.from_dict(workflow_response_model_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


