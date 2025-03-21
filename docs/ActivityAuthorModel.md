# ActivityAuthorModel


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
from openapi_client.models.activity_author_model import ActivityAuthorModel

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityAuthorModel from a JSON string
activity_author_model_instance = ActivityAuthorModel.from_json(json)
# print the JSON string representation of the object
print(ActivityAuthorModel.to_json())

# convert the object into a dict
activity_author_model_dict = activity_author_model_instance.to_dict()
# create an instance of ActivityAuthorModel from a dict
activity_author_model_from_dict = ActivityAuthorModel.from_dict(activity_author_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


