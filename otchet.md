# IO-bound

## Выполнение синхронно в один поток:
### Время выполнения:
![img.png](screens/img1.png)
### Диспетчер задач:
![img.png](screens/img.png)

## Выполнение используя ThreadPoolExecutor:
## max_workers = 5
### Время выполнения:
![img.png](screens/img4.png)
### Диспетчер задач:
![img.png](screens/img3.png)

## max_workers = 10
### Время выполнения:
![img.png](screens/img6.png)
### Диспетчер задач:
![img.png](screens/img5.png)

## max_workers = 100
### Время выполнения:
![img.png](screens/img8.png)
### Диспетчер задач:
![img.png](screens/img7.png)

## При преобразованиях время выполнения  заметно уменьшается, а загрузка памяти отличается буквально на пару процентов, процессор(цп) в основном тоже одинаков, но бывают некие скачки и получается заметное отличие

# CPU-bound

## Выполнение на одном ядре:
### Время выполнения:
![img_1.png](screens/img10.png)
### Диспетчер задач:
![img.png](screens/img9.png)

## Выполнение используя ProcessPoolExecutor:

## Воркер = 2:
### Время выполнения:
![img.png](screens/img12.png)
### Диспетчер задач:
![img.png](screens/img11.png)

## Воркер = 4:
### Время выполнения:
![img.png](screens/img14.png)
### Диспетчер задач:
![img.png](screens/img13.png)

## Воркер = 5:
### Время выполнения:
![img.png](screens/img16.png)
### Диспетчер задач:
![img.png](screens/img15.png)

# Воркер = 10:
### Время выполнения:
![img.png](screens/img18.png)
### Диспетчер задач:
![img.png](screens/img17.png)

## Воркер = 100:
![img.png](screens/img19.png)

## Сильно меняется загрузка процессора, время выполнения уменьшается с увеличением количества воркеров. Максимальное количество воркеров - 61 из-за особенностей ОС.