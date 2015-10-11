# Pretty compact JSON

Very simple tool that reads a [jsonl](https://en.wikipedia.org/wiki/JSON_Streaming#Line_delimited_JSON) file and outputs the same json objects, with the first level unfolded.


## Example

input:
```json
{"aa": "hello", "bb": [1, 2, 3], "cc": {"cat": 3, "car": 5}}
{"aa": "hello", "bb": [], "dd": {"dad": 2, "diy": 7}}
```

output:
```json
{
  "aa": "hello",
  "bb": [1, 2, 3],
  "cc": {"cat": 3, "car": 5}
}
{
  "aa": "hello",
  "bb": [],
  "dd": {"dad": 2, "diy": 7}
}
```
