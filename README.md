# 2023-10-hackaton-rutube

# Система Распознавание именованных сущностей в названиях и описанияхк видео
Хакатон цифровой прорыв

# Структура проекта
ai - модуль аналитики (pytorch, etc..)
backend - модуль бэкенда (django, etc...)

# Запуск проекта
git clone https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube
cd 2023-10-hackaton-rutube
docker-compose up --build
открыть http://localhost:80
# Остановка
docker compose down

# Установка docker-compose на ubuntu
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
"deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo apt-get update
sudo apt-get install docker-compose-plugin

sudo apt  install docker-compose

docker compose version

# Разработано командой RGB
ml: @aiMihail
front + design: @viktoriamityaeva
design + pm: @sofiyafil
backen/devops: @anfranchuk