# 누르면 카운트 증가, 카운트에 따라서 이미지 변경

#### 누르면 카운트 증가

- 카운트 증가

```html
<a href="{% url 'questions:count' choice.id 1 %}">{{question.pick_1}}</a>
```

- urls.py

```python
path('<int:choice_id>/<int:select>/count/', views.count, name='count'),
```

- views.py

```python
def count(request, choice_id, select):
    choice = Choice.objects.get(id=choice_id)
    if select == 1:
        choice.pick_1_count += 1
    else:
        choice.pick_2_count += 1

    choice.save()    

    return redirect('questions:detail', choice.question.id)

```

#### 카운트 확인

- 카운트 확인

```html
<p class="card-text" style="font-size: 3em; text-align:center;">{{question.choice_set.all.0.pick_1_count}}</p>
```



#### 카운트에 따라서 이미지 변경

- html

``` python
{% for choice in question.choice_set.all %}
  {% if choice.pick_1_count == choice.pick_2_count %}
```



#### 저번에 했지만 background-image줄때 꽉꽉 채워서 넣는 방법

- html

```html
<div style="background-image: url('/static/create.png'); width: 100%; height: 410px; background-size: cover; background-position: center;">
```



