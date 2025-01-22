const artikulInput = document.getElementById('artikulInput');
const infoButton = document.getElementById('infoButton');
const subscribeButton = document.getElementById('subscribeButton');
const resultDiv = document.getElementById('result');


infoButton.addEventListener('click', async () => {
    const artikul = artikulInput.value;
    if (artikul) {
        window.location.href = `/product.html?artikul=${artikul}`;
    }
});
unsubscribeButton.addEventListener('click', async () => {
    const artikul = artikulInput.value;
     try {
        const response = await fetch(`/api/v1/unsubscribe/${artikul}`, {
            method: 'GET',
        });
          if (response.ok) {
               resultDiv.textContent = 'Вы отменили подписку на обновления по товару';
          } else {
               resultDiv.textContent = 'Ошибка при оформлении подписки';
          }
     } catch (error) {
         resultDiv.textContent = 'Ошибка: ' + error;
     }
});

subscribeButton.addEventListener('click', async () => {
    const artikul = artikulInput.value;
     try {
        const response = await fetch(`/api/v1/subscribe/${artikul}`, {
            method: 'GET',
        });
          if (response.ok) {
               resultDiv.textContent = 'Вы подписаны на обновления по товару';
          } else {
               resultDiv.textContent = 'Ошибка при оформлении подписки';
          }
     } catch (error) {
         resultDiv.textContent = 'Ошибка: ' + error;
     }
});