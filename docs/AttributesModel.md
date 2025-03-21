# AttributesModel

The data that will be used to populate the workflow's fields. Learn more about the various attributes and their associated types by viewing the [Launch a Workflow](https://developer.ironcladapp.com/docs/launch-a-workflow) guide. Your attributes will differ and include more than this simple example.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_name** | **str** |  | 
**draft** | [**List[AttributesModelDraftInner]**](AttributesModelDraftInner.md) | Provide a URL for a file representing the first uploaded version of a counterparty paper. This field is required when the template source is set to third party paper | [optional] 
**paper_source** | **str** | Indicate the type of paper source used on a contract that supports both templatized and third party paper functionality. This field is required when there exists a question for selecting paper source on the template | [optional] 

## Example

```python
from openapi_client.models.attributes_model import AttributesModel

# TODO update the JSON string below
json = "{}"
# create an instance of AttributesModel from a JSON string
attributes_model_instance = AttributesModel.from_json(json)
# print the JSON string representation of the object
print(AttributesModel.to_json())

# convert the object into a dict
attributes_model_dict = attributes_model_instance.to_dict()
# create an instance of AttributesModel from a dict
attributes_model_from_dict = AttributesModel.from_dict(attributes_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


