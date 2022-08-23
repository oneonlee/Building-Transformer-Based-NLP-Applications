# Building-Transformer-Based-NLP-Applications

<div align="center">
  <img width=50% alt="DLI_Header" src="images/DLI_Header.png">

[NVIDIA DLI](https://www.nvidia.com/ko-kr/training/)의 "[Building Transformer-Based NLP Applications (Transformer 기반 자연어 처리 애플리케이션 구축)](https://www.nvidia.com/ko-kr/training/instructor-led-workshops/natural-language-processing/)" 워크숍 레포지토리

</div>

## 개발 환경

- [NVIDIA NGC](https://www.nvidia.com/ko-kr/gpu-cloud/)
- [JupyterLab](/00_jupyterlab.ipynb)

# 목차
## 1부: Machine Learning in NLP
### 1. [트랜스포머 아키텍처](010_Transformer-NLP.ipynb)<br>
- 트랜스포머 아키텍처
- 어텐션
- 인코더 피쳐
- 디코더 피쳐
### 2. [BERT](020_BERT.ipynb)<br>
- BERT 구조
- 토크나이저
- Contextualized Word Embedding
- Visualizing Attention with BERT
### 3. [언어 모델 사전 훈련](030_PretrainingLM.ipynb)
- 데이터 준비
- 토크나이저 학습
- NeMo와 BERT 사전훈련


## 2부: Self-Supervision, BERT, and Beyond (자기지도, BERT 및 최신 모델)
### 1. [데이터 살펴보기](010_ExploreData.ipynb)<br>
2개의 클래스 프로젝트에 레이블링된 PubMed Abstract 793개로 구성된 [NCBI 질병 언어 자료](https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/)에서 가져온 데이터세트를 사용합니다. 이러한 데이터세트의 세부 정보를 살펴보고 이런 유형의 애플리케이션에 맞춰 _자신의 데이터세트_  를 조정할 수 있는 방법에 대한 인사이트를 얻을 수 있습니다.<br>
다음과 같은 데이터를 살펴보게 됩니다.:
- Corpus Annotated Data (코퍼스 주석 처리된 데이터)
- 텍스트 분류 데이터 세트
- NER 데이터세트
<br><br>
### 2. [텍스트 분류자(Text Classifier) 구축하기(NVIDIA NeMo v1.0)](020_TextClassification.ipynb)<br>
[NVIDIA NeMo](https://developer.nvidia.com/nvidia-nemo) 오픈 소스 툴킷을 활용하여 BERT 기반 다중 클래스 분류 프로젝트를 구축할 예정입니다. 프레임워크는 [PyTorch Lightning](https://www.pytorchlightning.ai/)에 기반이 되어 있습니다.<br>
다음과 같은 내용을 배웁니다.:
- 텍스트 분류 프로젝트 구축 방법
- 커맨드 라인(명령줄)에서 실험(Experiment)을 빠르게 실행해 보는 방법
- PyTorch Lightning를 활용한 트레이닝 및 테스트 방법     
- 사전 훈련된 BERT 모델 선택 방법 
- 모델 정확도 시각화 방법
<br><br>
### 3. [명명된 엔티티 인식기 구축(NVIDIA NeMo v1.0)](030_NamedEntityRecognition.ipynb)<br>
NVIDIE Nemo를 활용하여 도메인별 명명된 엔티티 인식기(NER, named entitity recognition)을 구축할 예정입니다.<br>
다음과 같은 내용을 배웁니다.:
- 토큰 분류 (NER 태스크) 프로젝트 구축
- 커맨드 라인(명령줄)에서 토큰 분류기 트레이닝 
- 도메인별 모델 적용하기
- 저장된 체크포인트에서 NER 모델 테스트하기
<br><br>

## 3부: Production Deployment (프로덕션 배포)

---

# Certificates

<div align="center">

<a href="" target="_blank">
<img width=75% alt="Certificates" src="/images/Certificate.jpg"></a>

</div>
