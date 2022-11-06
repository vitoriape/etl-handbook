<h3 align="center"> 
  <img alt="etl_handbook banner" src="assets/etl_handbook.png" width="1000" height="400">
</h3>

<h1 align="center">
   <a href="#"> ETL HANDBOOK </a>
</h1>

<h3 align="center">
    ETL Work Model
</h3>


<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/vitoriape/etl-handbook?color=%23ff5c33">
  
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/vitoriape/etl-handbook">
  
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/vitoriape/etl-handbook?color=%ffff00">
  </a>
</p>

<h4 align="center"> 
	 Status: Ongoing
</h4>

---

Index
======
<!--ts-->
   * [About](#about)
   * [Tools](#tools)
   * [References](#references)
   * [Features](#features)
   * [Data Model](#data-model)
      * [Extract](#extract)
      * [Transform](#transform)
      * [Load](#load)
   * [Pre-requisites](#pre-requisites)
   * [Setup](#setup)
   * [Team](#team)

## About
Este projeto é um compilado de modelos e guias criados para auxliar na introdução ao modelo de trabalho ETL (Extract Transform Load). 

## Tools
O desenvolvimento desses códigos de teste utiliza as ferramentas abaixo:

- [Visual Studio Code](https://code.visualstudio.com/docs)
- [Excel 365](https://support.microsoft.com/en-us/excel)
- [MySQL Workbench 8.0.28](https://dev.mysql.com/downloads/workbench/)
- [Git 2.33.1](https://git-scm.com/downloads)
- [PowerBI Desktop](https://www.microsoft.com/pt-br/download/details.aspx?id=58494)

## References

| **Tool**       | **Documentation** 						                               |
|----------------|---------------------------------------------------------------------------------------------|
|   DAX          | [Referência de DAX](https://docs.microsoft.com/pt-br/dax/)     			       |
|   Visual Basic for Applications             |  [Excel and VBA Reference](https://docs.microsoft.com/en-us/office/vba/api/overview/excel)                 |
|      SQL          |      [SQL Reference](https://dev.mysql.com/doc/)             |
|       Power Query              | [Power Query Reference](https://learn.microsoft.com/en-us/power-query/) |

---

## Features

- [ ] Databases
- [x] Automation scripts
- [x] MER/ER templates
- [x] Formula tips
- [] Report models 


## Data Model
### **Extract**
Este modelo de trabalho utiliza a ferramenta **Power Query** para extração e leitura dos dados fonte.

### **Transform**
Parte da transformação dos dados é feita dentro da etapa anterior, mas a maior parte dos reparâmetros e normalizações são feitas dentro do **Excel** ou de um **SGBD**. O uso da linguagem **VBA** se dá para fins de automação de processos internos, que por sua vez também pode ser realizado com **Python**.

### **Load**
Resultado final da estação de trabalho, é o _insight_ dos dados. Nessa rotina os relatórios são finalizados por meio do **PowerBI** e seus arranjos em **DAX**.

---

## Pre-requisites


## Setup

I. Necessário possuir o Office 365 instalado 

II. Configure a [Guia Desenvolvedor](https://support.microsoft.com/pt-br/topic/mostrar-a-guia-desenvolvedor-e1192344-5e56-4d45-931b-e5fd9bea2d45) no Excel  

III. Instale o PowerBI

IV. Faça a instalação da extensão [Power Query \ M Language](https://marketplace.visualstudio.com/items?itemName=PowerQuery.vscode-powerquery) para maior facilidade de edição.


---

## Team
### Contributors
<table>
  <tr>
    <td align="center"><a href="https://github.com/vitoriape"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/55922652?v=4" width="100px;" alt=""/><br /><sub><b>Vitória Peçanha</b></sub></a><br /><a href="https://www.linkedin.com/in/vitoria-pecanha/" title="LinkedIn">🌐</a>   <a href="mailto:vitoriapecanha.log@gmail.com" title="E-mail">📬</a>   <a href="https://www.workana.com/pt/freelancer/adc45c752416bdaecd6e912140fe5fd3" title="Workana Profile">📊</a></td>
  </tr>
</table>
