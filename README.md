# Проект «Симуляция»
Симуляция 2D мира, населённого травоядными и хищниками. Кроме существ, мир содержит ресурсы (траву), которым питаются травоядные, и статичные объекты, с которыми нельзя взаимодействовать - они просто занимают место.

Приложение написано на языке Python в ООП-стиле. В поиске пути используется алгоритм поиска в ширину.
Техническое задание проекта: https://zhukovsd.github.io/java-backend-learning-course/Projects/Simulation/

## Игровые правила:
- львы ищут зебр, добираясь до клетки с целью – атакуют;
- у всех существ есть запас здоровья, у львов бонусом – сила урона;
- зебры ищут траву, сближаясь с ней – мгновенно съедают, но перед львами – они беззащитны;
- трава добавляет свинье небольшое количество здоровья;
- у существ есть скорость (сколько клеток они могут пройти за 1 итерацию), у львов она вдвое больше;
- у существ есть голод, при итерации без еды, их здоровье уменьшается;
- игра завершается после гибели всех зебр, львов, отсутствия достижимых целей или через паузу -> выход.

🦁 🦓 🥬 🌴 🗻

## Для успешного запуска приложения:
1. Откройте терминал
2. Перейдите в папку `main`
3. Запустите программу python `main.py`

<img width="273" alt="image" src="https://github.com/ekataeva/Sumulation/assets/110416537/9a7dd093-6cfc-4806-bc04-e05485f54a18">

<img width="280" alt="image" src="https://github.com/ekataeva/Sumulation/assets/110416537/d5238267-1603-4e82-a184-b7ef8b1c2041">

<img width="348" alt="image" src="https://github.com/ekataeva/Sumulation/assets/110416537/239d910e-f78d-4e66-9499-5451d6be3fc0">
