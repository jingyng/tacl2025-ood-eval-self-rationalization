# Self-Rationalization in the Wild: A Large Scale Out-of-Distribution Evaluation on NLI-related tasks
[![Arxiv](https://img.shields.io/badge/Arxiv-2502.04797-red?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.04797)
[![License](https://img.shields.io/github/license/jingyng/tacl2025-ood-eval-self-rationalization)](https://opensource.org/licenses/Apache-2.0)
[![Python Versions](https://img.shields.io/badge/Python-3.9-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CI](https://github.com/jingyng/tacl2025-ood-eval-self-rationalization/actions/workflows/main.yml/badge.svg)](https://github.com/jingyng/tacl2025-ood-eval-self-rationalization/actions/workflows/main.yml)

This is the project page for the TACL paper: Self-Rationalization in the Wild: A Large Scale Out-of-Distribution Evaluation on NLI-related tasks.

> **Abstract:** Free-text explanations are expressive and easy to understand, but many datasets lack annotated explanation data, making it challenging to train models for explainable predictions. To address this, we investigate how to use existing explanation datasets for self-rationalization and evaluate models' out-of-distribution (OOD) performance. We fine-tune T5-Large and OLMo-7B models and assess the impact of fine-tuning data quality, the number of fine-tuning samples, and few-shot selection methods. The models are evaluated on 19 diverse OOD datasets across three tasks: natural language inference (NLI), fact-checking, and hallucination detection in abstractive summarization. For the generated explanation evaluation, we conduct a human study on 13 selected models and study its correlation with the Acceptability score (T5-11B) and three other LLM-based reference-free metrics. Human evaluation shows that the Acceptability score correlates most strongly with human judgments, demonstrating its effectiveness in evaluating free-text explanations. Our findings reveal: 1) few annotated examples effectively adapt models for OOD explanation generation; 2) compared to sample selection strategies, fine-tuning data source has a larger impact on OOD performance; and 3) models with higher label prediction accuracy tend to produce better explanations, as reflected by higher Acceptability scores.

Contact person: [Jing Yang](mailto:jing.yang@tu-berlin.de) 

Don't hesitate to send us an e-mail or report an issue, if something is broken (and it shouldn't be) or if you have further questions.

## Cite

Please use the following citation:

```
@article{yang2025self,
  title={Self-Rationalization in the Wild: A Large-scale Out-of-Distribution Evaluation on NLI-related tasks},
  author={Yang, Jing and Glockner, Max and Rocha, Anderson and Gurevych, Iryna},
  journal={Transactions of the Association for Computational Linguistics},
  volume={13},
  pages={314--342},
  year={2025},
  publisher={MIT Press}
}
```

## Disclaimer

> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication. 
