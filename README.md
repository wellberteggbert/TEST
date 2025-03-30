[![CI/CD GitHub Actions](https://github.com/wellberteggbert/TEST/actions/workflows/python-app.yml/badge.svg)](https://github.com/wellberteggbert/TEST/actions/workflows/python-app.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wellberteggbert_TEST&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wellberteggbert_TEST)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=wellberteggbert_TEST&metric=bugs)](https://sonarcloud.io/summary/new_code?id=wellberteggbert_TEST)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=wellberteggbert_TEST&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=wellberteggbert_TEST)
# План функционального тестирования
1. Список функций для тестирования

      Тестированию подвергается одна функция вычисления корней квадратного уравнения
      solve_quadratic(a, b, c)
2. Подход

      Тестирование должно проходить в автоматическом режиме. В корневом каталоге проекта подготовлен файл test_quadratic_func.py.
      Все тесты входят в один класс TestQuadratic:
      - тест test_zero_a проверяет является ли уравнение квадратным;
      - тест test_standard_cases ожидает два корня уравнения при положительном дискриминанте; повторяющийся корень уравнения при нулевом дискриминанте;
      - тест  test_complex_roots ожидает два комплексных корня уравнения при положительном комплексном дискриминанте;
      - тест test_negative_discriminant ожидает нули в обоих корнях при отрицательном дискриминанте.
3. Критерии прохождения и провала

      Тестирование проводится сравнительным утверждением assertEqual(expected, actual);, результатом которого может быть критический отказ (fatal failure). В тестируемую функцию передаются входные параметры, а результаты ее работы сравниваются с ожидаемой величиной.
      Критерием прохождения теста является точное совпадение реальной и ожидаемой величин. 
      - Положительным прохожденим теста является запись 100% tests passed, 0 tests failed out of 1. 
      - В случае отрицательного результата запись будет иметь следующий вид Error: Process completed with exit code XX., также появятся записи вида [  FAILED  ], указывающие какой конкретно тест провален.
4. Результаты тестирования

      Все тесты должны проходить успешно.
5. Инструменты и ресурсы

      Основным инструментом проверки являются библиотеки`unittest`, `pytest` на платформе непрерывной интеграции и непрерывной доставки CI/CD GitHub Actions.
