# ray practice

## API 정보
|API|description|
|-------|--------|
|ray.init()|ray driver를 실행함. cpu,gpu number등 인자로 받음|
|@ray.remote|함수나 클래스를 다른 프로세스에서 실행시킬 수 있는 ray Task(Actor)로 바꿔주는 데코레이터 |
|.remote()|remote 함수나 클래스 호출시 뒤에 붙여 사용해야함. Asynchonous 실행 |
| ray.put()|obj store에 object저장 & ID반환, remote func호출시 인자로 사용가능. synchronous실행 |
|ray.get()|ObjectRef(Object ID)를 인자로 받아 object value를 반환함. synchronous실행 |
|ray.wait()|준비된 Obj id, 준비되지 않은 Obj id를 반환함. Task가 완료될 때까림지 기다|

## My Reference
- ray git repo : https://github.com/ray-project/ray
- ray paper 번역 : https://brunch.co.kr/@chris-song/106
- ray 기본 동작 설명 : https://dl4ab.github.io/2020/09/01/20200902-A-Quick-Tutorial-on-Ray/
- ray dashboard document : https://docs.ray.io/en/latest/ray-dashboard.html
- 꼭 읽기 (tips for first-time users) : https://docs.ray.io/en/master/auto_examples/tips-for-first-time.html
- Best practices(Ray with tensorflow) : https://docs.ray.io/en/master/using-ray-with-tensorflow.html
- Ray Design Patterns 보면서 안티 패턴 피하기 : https://docs.ray.io/en/master/using-ray-with-tensorflow.html
