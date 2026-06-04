# Building Recommender Systems Using Large Language Models

<table>
  <tr>
    <td style="width: 560px; vertical-align: top;">
      <img src="./images/frontcover.jpg" alt="Book Cover" width="540" style="border: 1px solid #ccc; border-radius: 4px;" />
    </td>
    <td style="vertical-align: middle; padding-left: 20px;">
      <p>This repository contains expanded tutorials and Python notebooks to accompany the book <em>Building Recommender Systems Using Large Language Models</em> by Jay.</p>
      <p>
        <a href="https://www.amazon.com/dp/B0FX7N91FQ/ref=tmm_kin_swatch_0" target="_blank" 
           style="background-color: #fff3b0; padding: 6px 10px; border-radius: 6px; font-weight: bold; text-decoration: none; color: #000;">
          📘 Order now from Amazon
        </a>
      </p>
    </td>
  </tr>
</table>



## About this repository

Within the chapter folders, you will find **eleven expanded tutorials** (with Chapter 1, 3, 4, and 7 containing two each), accompanied by Jupyter notebooks that walk through the code and experiments. 
| Chapter | Tutorial Title | Description |
|--------|----------------|-------------|
| 1 | [**Understanding Tokenization and Transformer Model**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter1/understanding_tokenization_transformer.ipynb) | Explores how LLM tokenization works and how transformer-based models process input. |
| 1 | [**Understanding Content Embedding and Retrieval**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter1/understanding_content_embedding_retrieval.ipynb) | Demonstrates how to generate embeddings and perform semantic retrieval. |
| 2 | [**From Traditional to LLM-Based Recommendations (MovieLens)**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter2/From_Traditional_to_LLM_Recommendation_Systems.ipynb) | Transitions from matrix factorization to LLM-augmented recommendation using the MovieLens dataset. |
| 3 | [**Topic Classification and Item Similarity Labeling Using LLMs**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter3/LLM_based_Data_Labeling.ipynb) | Uses LLMs to generate labels for item classification and similarity, aiding downstream recommendation. |
| 3 | [**News Recommendation with Embeddings and Learning-to-Rank**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter3/News_Recommendation_Learning_to_Rank.ipynb) | Combines embedding extraction with traditional learning-to-rank methods. |
| 4 | [**Fine-Tuning LLMs for Personalized Movie Recommendations**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter4/fine-tuning_LLMs_for_recommendation.ipynb) | Fine-tunes LLMs using preference data to deliver personalized movie recommendations. |
| 4 | [**Knowledge Distillation Using MovieLens Dataset**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter4/Distill_Recommendation_Capability_of_LLM.ipynb) | Distills a larger model into a smaller one using LLM-judged preference labels. |
| 5 | [**Conversational Recommendation System with RL and LLMs**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter5/Conversational_shopping_assistant.ipynb) | Builds a dialogue-based recommender using reinforcement learning and LLMs. |
| 6 | [**Multi-Modal Fashion Recommendation with Pairwise Ranking**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter6/Multi_Modal_Recommendation_Study.ipynb) | Uses CLIP embeddings and LLMs to build a fashion recommender from images and text. |
| 7 | [**Image-to-Avatar Generation**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter7/Image_to_avartar_generation.ipynb) | Transfer real user images into Ghibli and pixar styles and evaluate style transfer quality. |
| 7 | [**Goal-Driven Planning with LLMs**](https://github.com/qqwjq1981/springer-LLM-recommendation-system/blob/main/tutorials/Chapter7/MultiStep_Task_Decomposition_Recommendation.ipynb) | Demonstrates stepwise recommendation planning using reasoning-capable LLMs. |

---

## Setup

### 1. API keys (`curify_api.yaml`)

Most notebooks call OpenAI (and one — Chapter 3's `LLM_based_Data_Labeling` — also calls DeepSeek) via a single YAML config file named `curify_api.yaml`. Earlier editions of the notebooks hard-coded the author's local path (`./../../../Curify/curify_api.yaml`) — that's been replaced with a portable loader. To set it up:

```bash
cp config/curify_api.example.yaml curify_api.yaml
# then edit curify_api.yaml and paste in your real keys
```

The loader (`tutorials/_config.py`) searches in this order, so any of these works:

1. `$CURIFY_API_YAML` environment variable pointing at any path
2. `curify_api.yaml` at the repo root (the recommended location)
3. `config/curify_api.yaml`
4. `./../../../Curify/curify_api.yaml` (kept for the author's own setup)

The real `curify_api.yaml` is in `.gitignore` — never commit it. You only need `openai.api_key`; the `deepseek` entry is optional and used by exactly one notebook (skip its DeepSeek cells if you don't have a key).

### 2. Data files

Each notebook expects its data under a `Data/` directory sibling to `tutorials/` (i.e. `<repo>/Data/...`). These files are **not** committed — they're large and have their own licenses. Download what you need:

| Notebook | Expected path | How to get it |
|---|---|---|
| Ch1 `understanding_content_embedding_retrieval`, Ch3 `LLM_based_Data_Labeling`, Ch3 `News_Recommendation_Learning_to_Rank` | `Data/news-recommendation/news_summary.tsv` | Download from [Kaggle: News Summary](https://www.kaggle.com/datasets/sunnysai12345/news-summary) and place at the path shown |
| Ch2 `From_Traditional_to_LLM_Recommendation_Systems`, Ch4 `fine-tuning_LLMs_for_recommendation` | `Data/ml-1m/ratings.dat` | Download [MovieLens 1M](https://grouplens.org/datasets/movielens/1m/) and unzip so `Data/ml-1m/ratings.dat` exists |
| Ch6 `Multi-Modal_Retrieval_with_MS-COCO` | `captions_train2017.json` | Download [COCO 2017 annotations](https://cocodataset.org/#download) (`annotations_trainval2017.zip`) and either place it at the path the notebook references or update the `data_dir` constant near the top of the notebook to your local copy |

### 3. Running the notebooks

- Run cells **top-to-bottom in order** — later cells depend on names (`item_df`, `client`, `llm`, `plan_json`, etc.) defined by earlier cells. If you re-open a notebook and jump to a mid-chapter cell, restart the kernel and run from the beginning, or you'll see `NameError: name 'X' is not defined`.
- Each chapter directory is the intended working directory when you launch JupyterLab / VS Code. The shared loader at `tutorials/_config.py` is found because it's one directory above the notebook.

---

## About the book

Integrating Large Language Models (LLMs) into recommendation systems is transforming personalization, enabling deep context awareness and nuanced user understanding beyond traditional methods. As personalization becomes central to engagement and business growth, mastering LLM-driven approaches is essential.

This book covers:
- Fundamentals of LLMs and classic recommender systems  
- Techniques like tokenization, retrieval, fine-tuning, and embedding  
- Advanced topics: conversational recommenders, knowledge distillation, and multi-modal systems  
- Future trends, ethical challenges, and system-level implications  
- Practical, tutorial-driven implementations

Readers will be equipped to design, implement, and evaluate LLM-powered recommendation systems, and adapt the techniques to production use cases.

---

## About the author

**Jianqiang (Jay) Wang** is a seasoned data science professional with a Ph.D. in Statistics and extensive experience across academia and industry. Formerly a Principal Applied Science Manager at Microsoft, Jay has also served as Visiting Professor at Colorado State University, Data Scientist at Twitter, Lead Data Scientist at Snap, and Director of Data Science at Kuaishou. His expertise spans backend algorithms for search advertising, customer growth, inventory optimization, and ML education—particularly in internet platforms and retail innovation.

[LinkedIn](https://www.linkedin.com/in/jay-jianqiang-wang-78a6726/) | [MentorCruise](https://mentorcruise.com/mentor/jaywang/) 

[Order now from Amazon](https://www.amazon.com/dp/B0FX7N91FQ/ref=tmm_kin_swatch_0)
