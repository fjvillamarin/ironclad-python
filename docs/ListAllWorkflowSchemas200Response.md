# ListAllWorkflowSchemas200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[ListAllWorkflowSchemas200ResponseListInner]**](ListAllWorkflowSchemas200ResponseListInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflow_schemas200_response import ListAllWorkflowSchemas200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflowSchemas200Response from a JSON string
list_all_workflow_schemas200_response_instance = ListAllWorkflowSchemas200Response.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflowSchemas200Response.to_json())

# convert the object into a dict
list_all_workflow_schemas200_response_dict = list_all_workflow_schemas200_response_instance.to_dict()
# create an instance of ListAllWorkflowSchemas200Response from a dict
list_all_workflow_schemas200_response_from_dict = ListAllWorkflowSchemas200Response.from_dict(list_all_workflow_schemas200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


