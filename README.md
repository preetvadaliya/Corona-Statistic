<h1 align = "center">
  C O R O N A &nbsp;&nbsp; S T A T I S T I C
  <br>
  <img alt="GitHub Top Language" src="https://img.shields.io/static/v1?label=Made%20with&message=Python&color=red&logo=python&logoColor=white" />
  <img alt="GitHub Top Language" src="https://img.shields.io/static/v1?label=Python&message=3.7.7&color=red&logo=python&logoColor=white" />
  <img alt="GitHub Top Language" src="https://img.shields.io/static/v1?label=Use%20of&message=Web%20Scraping&color=red&logo=google-chrome&logoColor=white" />
  <img alt="GitHub Top Language" src="https://img.shields.io/static/v1?label=Made%20with&message=Selenium&color=red" />
</h1>


<p align="center">Simple Python programs to obtain real-time statistical data of coronaviruses.</p>

<br>
<br>

### How to use?
Download **CoronaStatus.py** file and add into your project.

<br>
<br>

### How to download selenium web driver?
Download web driver according your Chrome version.
You can download from [Download Link](https://chromedriver.chromium.org/downloads).

<br>
<br>

### E X A M P L E
```python

from CoronaStatus import CoronaStatus
status = CoronaStatus("your chrome driver path")

```

<br>
<br>

## M E T H O D S

#### getConfirmedInState( )
return total number of confirmed case in state.
```python

status.getConfirmedInState()

```

<br> 

#### getRecoveredInState( )
return total number of confirmed case in state.
```python

status.getRecoveredInState()

```

<br> 

#### getDeathsInState( )
return total number of death in state.
```python

status.getDeathsInState()

```

<br> 

#### getConfirmedInCountry( )
return total number of confirmed case in country.
```python

status.getConfirmedInCountry()

```

<br> 

#### getRecoveredInCountry( )
return total number of confirmed case in country.
```python

status.getRecoveredInCountry()

```

<br> 

#### getDeathsInWorld( )
return total number of death in world.
```python

status.getDeathsInWorld()

```

<br> 

#### getConfirmedInWorld( )
return total number of confirmed case in world.
```python

status.getConfirmedInWorld()

```

<br> 

#### getRecoveredInWorld( )
return total number of confirmed case in world.
```python

status.getRecoveredInWorld()

```

<br> 

#### getDeathsInWorld( )
return total number of death in world.
```python

status.getDeathsInWorld()

```

<br> 

#### getStateName( )
return your state name.
```python

status.getStateName()

```

<br> 

#### getCountryName( )
return your country name.
```python

status.getCountryName()

```