# CreatorEmailModel

The Ironclad user (must be a user in your Ironclad account) used to launch the workflow by using the user's email address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of value used to identify the user. | [optional] [default to 'email']
**email** | **str** | The email address of the Ironclad user. | [optional] 

## Example

```python
from openapi_client.models.creator_email_model import CreatorEmailModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorEmailModel from a JSON string
creator_email_model_instance = CreatorEmailModel.from_json(json)
# print the JSON string representation of the object
print(CreatorEmailModel.to_json())

# convert the object into a dict
creator_email_model_dict = creator_email_model_instance.to_dict()
# create an instance of CreatorEmailModel from a dict
creator_email_model_from_dict = CreatorEmailModel.from_dict(creator_email_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


