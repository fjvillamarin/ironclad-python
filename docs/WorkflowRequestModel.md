# WorkflowRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** | The identifier of the workflow template | 
**creator** | [**CreatorEmailModel**](CreatorEmailModel.md) |  | 
**attributes** | [**AttributesModel**](AttributesModel.md) |  | 

## Example

```python
from openapi_client.models.workflow_request_model import WorkflowRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRequestModel from a JSON string
workflow_request_model_instance = WorkflowRequestModel.from_json(json)
# print the JSON string representation of the object
print(WorkflowRequestModel.to_json())

# convert the object into a dict
workflow_request_model_dict = workflow_request_model_instance.to_dict()
# create an instance of WorkflowRequestModel from a dict
workflow_request_model_from_dict = WorkflowRequestModel.from_dict(workflow_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


