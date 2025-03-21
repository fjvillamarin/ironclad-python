# ExternalUserModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**display_name** | **str** |  | [optional] 
**email** | **str** |  | 
**company_name** | **str** |  | 

## Example

```python
from openapi_client.models.external_user_model import ExternalUserModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalUserModel from a JSON string
external_user_model_instance = ExternalUserModel.from_json(json)
# print the JSON string representation of the object
print(ExternalUserModel.to_json())

# convert the object into a dict
external_user_model_dict = external_user_model_instance.to_dict()
# create an instance of ExternalUserModel from a dict
external_user_model_from_dict = ExternalUserModel.from_dict(external_user_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


