# ListAllWorkflows200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**page_size** | **int** |  | [optional] [default to 0]
**count** | **int** |  | [optional] [default to 0]
**list** | [**List[WorkflowResponseModel]**](WorkflowResponseModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflows200_response import ListAllWorkflows200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflows200Response from a JSON string
list_all_workflows200_response_instance = ListAllWorkflows200Response.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflows200Response.to_json())

# convert the object into a dict
list_all_workflows200_response_dict = list_all_workflows200_response_instance.to_dict()
# create an instance of ListAllWorkflows200Response from a dict
list_all_workflows200_response_from_dict = ListAllWorkflows200Response.from_dict(list_all_workflows200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


