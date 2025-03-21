# WorkflowLastModifiedAuthorModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**display_name** | **str** |  | 
**email** | **str** |  | 
**user_id** | **str** |  | 
**company_name** | **str** |  | 

## Example

```python
from openapi_client.models.workflow_last_modified_author_model import WorkflowLastModifiedAuthorModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowLastModifiedAuthorModel from a JSON string
workflow_last_modified_author_model_instance = WorkflowLastModifiedAuthorModel.from_json(json)
# print the JSON string representation of the object
print(WorkflowLastModifiedAuthorModel.to_json())

# convert the object into a dict
workflow_last_modified_author_model_dict = workflow_last_modified_author_model_instance.to_dict()
# create an instance of WorkflowLastModifiedAuthorModel from a dict
workflow_last_modified_author_model_from_dict = WorkflowLastModifiedAuthorModel.from_dict(workflow_last_modified_author_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


