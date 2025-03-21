# LaunchedWorkflowModelCreator



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**email** | **str** |  | [optional] [readonly] 
**display_name** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.launched_workflow_model_creator import LaunchedWorkflowModelCreator

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchedWorkflowModelCreator from a JSON string
launched_workflow_model_creator_instance = LaunchedWorkflowModelCreator.from_json(json)
# print the JSON string representation of the object
print(LaunchedWorkflowModelCreator.to_json())

# convert the object into a dict
launched_workflow_model_creator_dict = launched_workflow_model_creator_instance.to_dict()
# create an instance of LaunchedWorkflowModelCreator from a dict
launched_workflow_model_creator_from_dict = LaunchedWorkflowModelCreator.from_dict(launched_workflow_model_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


