# ApprovalRequests200ResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**actor_id** | **str** |  | [optional] 
**actor_type** | **str** |  | [optional] 
**actor_details** | **object** |  | [optional] 
**role** | **str** |  | [optional] 
**role_name** | **str** |  | [optional] 
**approval_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.approval_requests200_response_list_inner import ApprovalRequests200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequests200ResponseListInner from a JSON string
approval_requests200_response_list_inner_instance = ApprovalRequests200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequests200ResponseListInner.to_json())

# convert the object into a dict
approval_requests200_response_list_inner_dict = approval_requests200_response_list_inner_instance.to_dict()
# create an instance of ApprovalRequests200ResponseListInner from a dict
approval_requests200_response_list_inner_from_dict = ApprovalRequests200ResponseListInner.from_dict(approval_requests200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


