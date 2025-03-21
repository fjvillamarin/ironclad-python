# InternalUserModel


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
from openapi_client.models.internal_user_model import InternalUserModel

# TODO update the JSON string below
json = "{}"
# create an instance of InternalUserModel from a JSON string
internal_user_model_instance = InternalUserModel.from_json(json)
# print the JSON string representation of the object
print(InternalUserModel.to_json())

# convert the object into a dict
internal_user_model_dict = internal_user_model_instance.to_dict()
# create an instance of InternalUserModel from a dict
internal_user_model_from_dict = InternalUserModel.from_dict(internal_user_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


