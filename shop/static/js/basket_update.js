document.addEventListener('click', function(event) {
    var target = event.target;

    if (target.matches('.ajax-link')) {
        event.preventDefault();
        // Получаем активный элемент li из .size
        var activeElement = document.querySelector('.size li.active');
        var activeText = activeElement ? activeElement.innerHTML : null;
        

        // Добавляем красную обводку каждому элементу li внутри .size, если activeElement равен null
        if (!activeElement) {
            var sizeItems = document.querySelectorAll('.size li');
            sizeItems.forEach(function(item) {
                item.classList.add('red-outline');
            });

            setTimeout(function() {
                sizeItems.forEach(function(item) {
                    item.classList.remove('red-outline');
                });
            }, 2000); // Через 2 секунды убираем обводку
        } else {
            sendAjaxRequest(target.dataset.href, activeText);
        }
    }
});



// Получаем коллекцию всех элементов li
const liElements = document.querySelectorAll('.size li');

// Перебираем все элементы li и назначаем обработчик события на каждый
liElements.forEach(function(li) {
    li.addEventListener('click', function() {
        // Удаляем класс "active" у всех элементов li
        liElements.forEach(function(el) {
            el.classList.remove('active');
        });

        // Добавляем класс "active" только выбранному элементу li
        li.classList.add('active');

        // Получаем активный текст
        var activeText = li.innerHTML;
        
        // Вызываем функцию отправки AJAX-запроса с активным текстом
        sendAjaxRequest(this.dataset.href, activeText);
    });
});

function sendAjaxRequest(href, activeText) {
    // Строим ссылку с добавлением активного текста через двоеточие
    var url = window.location.origin + href;

    if (activeText && activeText.trim() !== '') {
        if (url.includes('?')) {
            url += '&size=' + encodeURIComponent(activeText);
        } else {
            url += '?size=' + encodeURIComponent(activeText);
        }
    }

    // Отправляем AJAX-запрос на сервер
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Обработка успешного ответа от сервера
            var response = xhr.responseText;

            var parser = new DOMParser();
            var doc = parser.parseFromString(response, 'text/html');

            // Находим объект .basket-btns в полученном документе
            var basketBtns = doc.querySelector('.basket-btns-data');

            var basketBtnsElement = document.querySelector('.basket-btns-data');
            basketBtnsElement.replaceWith(basketBtns);
        } else {
            // Обработка ошибок или других статусов ответа
        }
    };
    xhr.send();
}
