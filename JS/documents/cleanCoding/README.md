## 클린코딩이란 무엇일까

```“I like my code to be elegant and efficient.
The logic should be straightforward and make it hard for bugs to hide,
the dependencies minimal to ease maintenance, error handling complete according to an articulated strategy,
and performance close to optimal so as not to tempt people to make the code messy with unprincipled optimizations.
Clean code does one thing well.”
- Bjarne Stroustrup, inventor of ‘C++
```

“저는 제 코드가 우아하고 효율적이기를 원합니다. 논리는 직관적이며 버그를 찾아내기 쉽고, 유지보수하기쉬운 최소한의 종속성,
명료 한 전략에 따른 에러핸들링, 최적에 가까운 성능을 제공하며 원칙없는 코드로 혼란스럽지않도록 합니다. 깨끗한 코드는 한 가지 일에 집중합니다.”

단순하고 직관적이며 원작자의 의도를 숨기지않는 코드 -가독성

### 클린코드의 원칙

#### GENERAL

##### Follow Standard Conventions

```
Coding 표준, 아키텍쳐 표준 및 설계 가이드를 준수하라
```

##### Keep it Simple, Stupid(KISS)

```
단순한 것이 효율적이며, 복잡함을 최소화하라
```

##### Boy Scout Rule

```
캠핑장을 떠나기 전에 원래보다 깨끗하게 해야한다.
-참조되거나 수정되는 코드는 원래보다 clean하게 해야함
```

##### Root Cause Analysis

```
항상 근본적인 원인을 찾아라. 그렇지 않으면 반복될 것이다.
```

##### Do Not Multiple Languages in One Source File

```
하나의 파일은 하나의 언어로 작성하라
html in php
what the hell.....
```

#### Class Design - SOLID

##### Simple Responsibility Principle(SRP)

```
하나의 클래스는 하나의 책임만 가져야 한다
```

##### Open/Closed Principle(OCP)

```
클래스는 확장에 대하여 열려 있어야 하고,
변경에 대해서는 닫혀 있어야 한다.
```

##### Liskov Substitution Principle(LSP)

```
파생 클래스의 메소드는 기반 클래스의 메서드를
대체하여 사용될 수 있어야 한다.
```

##### Interface Segregation Principle(ISP)

```
클라이언트가 사용하지 않는 메소드에 의존하지 않아야 한다.
```

##### Dependency Inversion Principle(DIP)

```
추상화 된 것은 구체적인 것에 의존하면 안된다.
-자주 변경되는 구체적인 것에 의존하지 않고 추상화 된 것을 참조
```
