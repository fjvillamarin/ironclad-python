# CreatorIdModel

The Ironclad user (must be a user in your Ironclad account) used to launch the workflow by using the user's ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of value used to identify the user. | [optional] [default to 'id']
**id** | **str** | The user ID of the Ironclad user. | [optional] 

## Example

```python
from openapi_client.models.creator_id_model import CreatorIdModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorIdModel from a JSON string
creator_id_model_instance = CreatorIdModel.from_json(json)
# print the JSON string representation of the object
print(CreatorIdModel.to_json())

# convert the object into a dict
creator_id_model_dict = creator_id_model_instance.to_dict()
# create an instance of CreatorIdModel from a dict
creator_id_model_from_dict = CreatorIdModel.from_dict(creator_id_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


