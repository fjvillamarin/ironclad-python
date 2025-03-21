# RetrieveEmailThreadsFromWorkflow200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**page_size** | **int** |  | [optional] [default to 20]
**count** | **int** |  | [optional] 
**list** | [**List[EmailResponseModel]**](EmailResponseModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.retrieve_email_threads_from_workflow200_response import RetrieveEmailThreadsFromWorkflow200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEmailThreadsFromWorkflow200Response from a JSON string
retrieve_email_threads_from_workflow200_response_instance = RetrieveEmailThreadsFromWorkflow200Response.from_json(json)
# print the JSON string representation of the object
print(RetrieveEmailThreadsFromWorkflow200Response.to_json())

# convert the object into a dict
retrieve_email_threads_from_workflow200_response_dict = retrieve_email_threads_from_workflow200_response_instance.to_dict()
# create an instance of RetrieveEmailThreadsFromWorkflow200Response from a dict
retrieve_email_threads_from_workflow200_response_from_dict = RetrieveEmailThreadsFromWorkflow200Response.from_dict(retrieve_email_threads_from_workflow200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


