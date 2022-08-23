# Building-Transformer-Based-NLP-Applications

<div align="center">
  <img width=50% alt="DLI_Header" src="images/DLI_Header.png">

[NVIDIA DLI](https://www.nvidia.com/ko-kr/training/)의 "[Building Transformer-Based NLP Applications (Transformer 기반 자연어 처리 애플리케이션 구축)](https://www.nvidia.com/ko-kr/training/instructor-led-workshops/natural-language-processing/)" 워크숍 레포지토리

</div>

## 개발 환경

- [NVIDIA NGC](https://www.nvidia.com/ko-kr/gpu-cloud/)
- [NVIDIA NeMo](https://developer.nvidia.com/nvidia-nemo)
- JupyterLab

# 목차
## 1부: Machine Learning in NLP
### 1. [트랜스포머 아키텍처](010_Transformer.ipynb)<br>
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

사용 전, [`bert_qa.pt` data를 클릭하여 다운](https://www.dropbox.com/s/g9ymmvc73mp0r4s/bert_qa.pt?dl=0) 받아 `data` 폴더 안에 넣어주세요.


### 1. [모델 내보내기](010_ExportingTheModel.ipynb)<br/>
다음과 같은 내용을 배웁니다.
- PyTorch에서 트레이닝된 모델을 서버 효율적인 형식으로 변환<br/>
- 감소된 정밀도 및 TensorRT 모델 최적화 적용 <br/>
### 2. [모델 호스팅](020_HostingTheModel.ipynb)<br/>
다음과 같은 내용을 배웁니다.
- NVIDIA Triton Inference Server를 사용하여 프로덕션에 모델 배포<br/>
- 모델 구성을 통해 NVIDIA Triton의 일부 기본 기능 제어 <br/>
- 내보내기 형식 및 구성 옵션이 성능 및 비용에 미치는 영향 평가<br/>
### 3. [서버 성능](030_ServerPerformance.ipynb)<br/>
다음과 같은 내용을 배웁니다.
- 다양한 Triton 구성 옵션이 서빙 성능에 미치는 영향 평가<br/>
- 프로덕션의 추론 성능 모니터링 <br/>
### 4. [모델 사용](040_UsingTheModel.ipynb)<br/>
다음과 같은 내용을 배웁니다.
- Triton에서 노출되는 API를 활용할 수 있는 단순한 애플리케이션 구축<br/>
- 더 복잡한 애플리케이션 및 모델 파이프라인 배포를 위한 옵션 논의<br/>

---

# Certificates

<div align="center">

<a href="https://courses.nvidia.com/certificates/3635de0b089446bb8e95c101b05518e4/" target="_blank">
<img width=75% alt="Certificates" src="/images/Certificate.jpg"></a>

</div>
