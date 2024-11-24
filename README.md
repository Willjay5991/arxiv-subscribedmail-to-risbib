## 处理每天arxiv订阅邮件为bib、ris文件

**需求：**订阅了arxiv的论文推送提醒，每天都会收到最新论文的推送邮件，但是邮件都是文本格式的，不方便导入论文管理软件（endnote等），使用python脚本，提取arxiv推送邮件中每个论文的条目信息，转为方便管理的RIS或者Bibtex格式。

**功能**：

- [x] 从订阅的arxiv邮件中，提取论文的信息，生成bib文件或者Ris文件，供zotero或者endnote导入

**用法：**

1. 将邮件内容复制到txt文件中，命名为`arxiv.txt` ，
2. 将`arxiv.txt`文件放在 `processArxiv.py`同目录下，
3. 根据需求修改，line 103： `mode="xxx"`，选择对应的输出格式 

两种运行方式

1. 运行`processArxiv.py`文件，同目录下会出现`arxiv.ris`

2. windows bat命令： 直接双击 `run.bat`, 同目录下会出现`arxiv.ris`









需要手动将邮件内容复制到txt文件中，处理后的txt文本内容如下：

**举例**

### 处理前

`24-8-arxiv.txt`:

```
------------------------------------------------------------------------------
------------------------------------------------------------------------------
Send any comments regarding submissions directly to submitter.
------------------------------------------------------------------------------
Archives at http://arxiv.org/
To unsubscribe, e-mail To: cs@arXiv.org, Subject: cancel
------------------------------------------------------------------------------
Submissions to:
Artificial Intelligence
Computer Vision and Pattern Recognition
Machine Learning
received from  Wed 20 Nov 24 19:00:00 GMT  to  Thu 21 Nov 24 19:00:00 GMT
------------------------------------------------------------------------------
------------------------------------------------------------------------------
\\
arXiv:2411.13560
Date: Thu, 7 Nov 2024 02:49:53 GMT   (31214kb,D)

Title: AMSnet-KG: A Netlist Dataset for LLM-based AMS Circuit Auto-Design Using
  Knowledge Graph RAG
Authors: Yichen Shi, Zhuofu Tao, Yuhao Gao, Tianjia Zhou, Cheng Chang, Yaxing
  Wang, Bingyu Chen, Genhao Zhang, Alvin Liu, Zhiping Yu, Ting-Jung Lin, Lei He
Categories: cs.AI cs.ET eess.SP
\\
  High-performance analog and mixed-signal (AMS) circuits are mainly
full-custom designed, which is time-consuming and labor-intensive. A
significant portion of the effort is experience-driven, which makes the
automation of AMS circuit design a formidable challenge. Large language models
(LLMs) have emerged as powerful tools for Electronic Design Automation (EDA)
applications, fostering advancements in the automatic design process for
large-scale AMS circuits. However, the absence of high-quality datasets has led
to issues such as model hallucination, which undermines the robustness of
automatically generated circuit designs. To address this issue, this paper
introduces AMSnet-KG, a dataset encompassing various AMS circuit schematics and
netlists. We construct a knowledge graph with annotations on detailed
functional and performance characteristics. Facilitated by AMSnet-KG, we
propose an automated AMS circuit generation framework that utilizes the
comprehensive knowledge embedded in LLMs. We first formulate a design strategy
(e.g., circuit architecture using a number of circuit components) based on
required specifications. Next, matched circuit components are retrieved and
assembled into a complete topology, and transistor sizing is obtained through
Bayesian optimization. Simulation results of the netlist are fed back to the
LLM for further topology refinement, ensuring the circuit design specifications
are met. We perform case studies of operational amplifier and comparator design
to verify the automatic design flow from specifications to netlists with
minimal human effort. The dataset used in this paper will be open-sourced upon
publishing of this paper.
\\ ( https://arxiv.org/abs/2411.13560 , 31214kb)
------------------------------------------------------------------------------
\\
arXiv:2411.13566
Date: Mon, 11 Nov 2024 10:35:41 GMT   (9474kb,D)

Title: Integrated Water Resource Management in the Segura Hydrographic Basin:
  An Artificial Intelligence Approach
Authors: Urtzi Otamendi, Mikel Maiza, Igor G. Olaizola, Basilio Sierra, Markel
  Flores, Marco Quartulli
Categories: cs.AI
Comments: 15 pages, 14 figures, 8 tables
ACM-class: J.m; I.2.1; I.4.9
Journal-ref: Journal of Environmental Management, Volume 370, 2024, ISSN
  0301-4797
DOI: 10.1016/j.jenvman.2024.122526
\\
  Managing resources effectively in uncertain demand, variable availability,
and complex governance policies is a significant challenge. This paper presents
a paradigmatic framework for addressing these issues in water management
scenarios by integrating advanced physical modelling, remote sensing
techniques, and Artificial Intelligence algorithms. The proposed approach
accurately predicts water availability, estimates demand, and optimizes
resource allocation on both short- and long-term basis, combining a
comprehensive hydrological model, agronomic crop models for precise demand
estimation, and Mixed-Integer Linear Programming for efficient resource
distribution. In the study case of the Segura Hydrographic Basin, the approach
successfully allocated approximately 642 million cubic meters ($hm^3$) of water
over six months, minimizing the deficit to 9.7% of the total estimated demand.
The methodology demonstrated significant environmental benefits, reducing CO2
emissions while optimizing resource distribution. This robust solution supports
informed decision-making processes, ensuring sustainable water management
across diverse contexts. The generalizability of this approach allows its
adaptation to other basins, contributing to improved governance and policy
implementation on a broader scale. Ultimately, the methodology has been
validated and integrated into the operational water management practices in the
Segura Hydrographic Basin in Spain.
\\ ( https://arxiv.org/abs/2411.13566 , 9474kb)
------------------------------------------------------------------------------
```



### 处理后：

`mode=bib` :

---

```
@article{arXiv:2411.13560,
  title = {AMSnet-KG: A Netlist Dataset for LLM-based AMS Circuit Auto-Design Using},
  author = {Shi, Yichen and Tao, Zhuofu and Gao, Yuhao and Zhou, Tianjia and Chang, Cheng and Yaxing, Yaxing},
  journal = {arXiv preprint arXiv:2411.13560 },
  year = {2024},
  url = {https://arxiv.org/abs/arXiv:2411.13560},
  abstract = {High-performance analog and mixed-signal (AMS) circuits are mainly
full-custom designed, which is time-consuming and labor-intensive. A
significant portion of the effort is experience-driven, which makes the
automation of AMS circuit design a formidable challenge. Large language models
(LLMs) have emerged as powerful tools for Electronic Design Automation (EDA)
applications, fostering advancements in the automatic design process for
large-scale AMS circuits. However, the absence of high-quality datasets has led
to issues such as model hallucination, which undermines the robustness of
automatically generated circuit designs. To address this issue, this paper
introduces AMSnet-KG, a dataset encompassing various AMS circuit schematics and
netlists. We construct a knowledge graph with annotations on detailed
functional and performance characteristics. Facilitated by AMSnet-KG, we
propose an automated AMS circuit generation framework that utilizes the
comprehensive knowledge embedded in LLMs. We first formulate a design strategy
(e.g., circuit architecture using a number of circuit components) based on
required specifications. Next, matched circuit components are retrieved and
assembled into a complete topology, and transistor sizing is obtained through
Bayesian optimization. Simulation results of the netlist are fed back to the
LLM for further topology refinement, ensuring the circuit design specifications
are met. We perform case studies of operational amplifier and comparator design
to verify the automatic design flow from specifications to netlists with
minimal human effort. The dataset used in this paper will be open-sourced upon
publishing of this paper.
\\ ( https://arxiv.org/abs/2411.13560 , 31214kb)}
}

@article{arXiv:2411.13566,
  title = {Integrated Water Resource Management in the Segura Hydrographic Basin:},
  author = {Otamendi, Urtzi and Maiza, Mikel and Olaizola, Igor G. and Sierra, Basilio and Markel, Markel},
  journal = {arXiv preprint arXiv:2411.13566 },
  year = {2024},
  url = {https://arxiv.org/abs/arXiv:2411.13566},
  abstract = {Managing resources effectively in uncertain demand, variable availability,
and complex governance policies is a significant challenge. This paper presents
a paradigmatic framework for addressing these issues in water management
scenarios by integrating advanced physical modelling, remote sensing
techniques, and Artificial Intelligence algorithms. The proposed approach
accurately predicts water availability, estimates demand, and optimizes
resource allocation on both short- and long-term basis, combining a
comprehensive hydrological model, agronomic crop models for precise demand
estimation, and Mixed-Integer Linear Programming for efficient resource
distribution. In the study case of the Segura Hydrographic Basin, the approach
successfully allocated approximately 642 million cubic meters ($hm^3$) of water
over six months, minimizing the deficit to 9.7% of the total estimated demand.
The methodology demonstrated significant environmental benefits, reducing CO2
emissions while optimizing resource distribution. This robust solution supports
informed decision-making processes, ensuring sustainable water management
across diverse contexts. The generalizability of this approach allows its
adaptation to other basins, contributing to improved governance and policy
implementation on a broader scale. Ultimately, the methodology has been
validated and integrated into the operational water management practices in the
Segura Hydrographic Basin in Spain.
\\ ( https://arxiv.org/abs/2411.13566 , 9474kb)}
}


```



`mode="ris"`

---

```
TY  - JOUR
TI  - AMSnet-KG: A Netlist Dataset for LLM-based AMS Circuit Auto-Design Using
AU  - Shi, Yichen and Tao, Zhuofu and Gao, Yuhao and Zhou, Tianjia and Chang, Cheng and Yaxing, Yaxing
JO  - arXiv preprint arXiv:2411.13560
PY  - 2024
UR  - https://arxiv.org/abs/arXiv:2411.13560
AB  - High-performance analog and mixed-signal (AMS) circuits are mainly
full-custom designed, which is time-consuming and labor-intensive. A
significant portion of the effort is experience-driven, which makes the
automation of AMS circuit design a formidable challenge. Large language models
(LLMs) have emerged as powerful tools for Electronic Design Automation (EDA)
applications, fostering advancements in the automatic design process for
large-scale AMS circuits. However, the absence of high-quality datasets has led
to issues such as model hallucination, which undermines the robustness of
automatically generated circuit designs. To address this issue, this paper
introduces AMSnet-KG, a dataset encompassing various AMS circuit schematics and
netlists. We construct a knowledge graph with annotations on detailed
functional and performance characteristics. Facilitated by AMSnet-KG, we
propose an automated AMS circuit generation framework that utilizes the
comprehensive knowledge embedded in LLMs. We first formulate a design strategy
(e.g., circuit architecture using a number of circuit components) based on
required specifications. Next, matched circuit components are retrieved and
assembled into a complete topology, and transistor sizing is obtained through
Bayesian optimization. Simulation results of the netlist are fed back to the
LLM for further topology refinement, ensuring the circuit design specifications
are met. We perform case studies of operational amplifier and comparator design
to verify the automatic design flow from specifications to netlists with
minimal human effort. The dataset used in this paper will be open-sourced upon
publishing of this paper.
\\ ( https://arxiv.org/abs/2411.13560 , 31214kb)
ER  - 

TY  - JOUR
TI  - Integrated Water Resource Management in the Segura Hydrographic Basin:
AU  - Otamendi, Urtzi and Maiza, Mikel and Olaizola, Igor G. and Sierra, Basilio and Markel, Markel
JO  - arXiv preprint arXiv:2411.13566
PY  - 2024
UR  - https://arxiv.org/abs/arXiv:2411.13566
AB  - Managing resources effectively in uncertain demand, variable availability,
and complex governance policies is a significant challenge. This paper presents
a paradigmatic framework for addressing these issues in water management
scenarios by integrating advanced physical modelling, remote sensing
techniques, and Artificial Intelligence algorithms. The proposed approach
accurately predicts water availability, estimates demand, and optimizes
resource allocation on both short- and long-term basis, combining a
comprehensive hydrological model, agronomic crop models for precise demand
estimation, and Mixed-Integer Linear Programming for efficient resource
distribution. In the study case of the Segura Hydrographic Basin, the approach
successfully allocated approximately 642 million cubic meters ($hm^3$) of water
over six months, minimizing the deficit to 9.7% of the total estimated demand.
The methodology demonstrated significant environmental benefits, reducing CO2
emissions while optimizing resource distribution. This robust solution supports
informed decision-making processes, ensuring sustainable water management
across diverse contexts. The generalizability of this approach allows its
adaptation to other basins, contributing to improved governance and policy
implementation on a broader scale. Ultimately, the methodology has been
validated and integrated into the operational water management practices in the
Segura Hydrographic Basin in Spain.
\\ ( https://arxiv.org/abs/2411.13566 , 9474kb)
ER  - 


```

