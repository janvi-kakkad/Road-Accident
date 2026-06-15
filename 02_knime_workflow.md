# KNIME Workflow Breakdown

Source workflow package: knime/KNIME_project3.knwf

## Pipeline Stages

1. Ingestion and cleaning
- CSV Reader (#2)
- Missing Value (#29)
- String Manipulation Multi Column (#28)
- Missing Value (#30)

2. EDA and reporting branches from cleaned table
- CSV Writer (#31)
- Statistics (#32)
- Conditional Box Plot (#34)
- String Manipulation (#37) -> Cell Splitter (#39) -> Math Formula (#40)
- Expression (#49) -> GroupBy (#50), Bar Chart (#51), Column Filter (#54)
- Pivot (#52) -> Heatmap (#53)
- Python Script nodes (#45/#46/#47/#48) for Chi-square tests

3. Correlation branch
- Math Formula (#40) -> Linear Correlation (#35)
- Math Formula (#40) -> Expression (#44) -> Rank Correlation (#42)

4. ML branch
- Column Filter (#54) -> Table Partitioner (#55)
- Table Partitioner -> Random Forest Learner (#56) and Decision Tree Learner (#57)
- Learners + partition output -> Predictors (#58/#60)
- Predictors -> Scorer (#59/#61)

## Workflow Visual

- SVG: output/knime/KNIME_workflow.svg

## Modeling Target

- Target column: Accident_severity
- Prediction columns: Prediction (Accident_severity)
