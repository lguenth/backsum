---
license: cc-by-4.0
language:
- en
configs:
- config_name: default
  data_files:
  - split: train
    path: "train.jsonl"
  - split: test
    path: "test.jsonl"
---

# Dataset Card for `backsum`

## Licensing

This dataset was derived from the [Scisumm Corpus](https://github.com/WING-NUS/scisumm-corpus).

If you use this data, please cite the original CL-SciSumm overview paper:
```
@inproceedings{
	title        = {Overview and Results: CL-SciSumm Shared Task 2019},
	author       = {Chandrasekaran, Muthu Kumar and Yasunaga, Michihiro and Radev, Dragomir and Freitag, Dayne and Kan, Min-Yen},
	year         = 2019,
	booktitle    = {In Proceedings of Joint Workshop on Bibliometric-enhanced Information Retrieval and NLP for Digital Libraries (BIRNDL 2019)}
}
```
