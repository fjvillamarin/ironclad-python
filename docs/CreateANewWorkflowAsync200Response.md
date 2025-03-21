# CreateANewWorkflowAsync200Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**async_job_id** | **str** |  | [readonly] 
**async_job_status_url** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.create_a_new_workflow_async200_response import CreateANewWorkflowAsync200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateANewWorkflowAsync200Response from a JSON string
create_a_new_workflow_async200_response_instance = CreateANewWorkflowAsync200Response.from_json(json)
# print the JSON string representation of the object
print(CreateANewWorkflowAsync200Response.to_json())

# convert the object into a dict
create_a_new_workflow_async200_response_dict = create_a_new_workflow_async200_response_instance.to_dict()
# create an instance of CreateANewWorkflowAsync200Response from a dict
create_a_new_workflow_async200_response_from_dict = CreateANewWorkflowAsync200Response.from_dict(create_a_new_workflow_async200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


