---
license: cc-by-4.0
language:
- en
configs:
- config_name: default
  data_files:
  - split: train
    path: "train.csv"
  - split: test
    path: "test.csv"
---

# Dataset Card for `backsum`

## Licensing

This dataset was derived from the [Scisumm Corpus](https://github.com/WING-NUS/scisumm-corpus).

If you use this data, please cite the original CL-SciSumm overview paper:
```
@inproceedings{,<br>
title={Overview and Results: CL-SciSumm Shared Task 2019},<br>
author={Chandrasekaran, Muthu Kumar and Yasunaga, Michihiro and Radev, Dragomir and Freitag, Dayne and Kan, Min-Yen},<br>
booktitle={In Proceedings of Joint Workshop on Bibliometric-enhanced Information Retrieval and NLP for Digital Libraries (BIRNDL 2019)},<br>
year={2019}<br>
}<br>
```