import vk_api
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def scrape_wall_data(token, owner_id, count=10):
    """
    Функция производит парсинг данных со стены сообщества ВКонтакте.
    
    """
    try:
        # Инициализация VK API
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        
        # Метод wall.get
        posts = vk.wall.get(owner_id=owner_id, count=count)['items']
        
        # Хранилище для данных
        scraped_data = []
        
        # Парсинг
        for post in posts:
            post_data = {}
            
            # Извлечение id поста
            post_data['post_id'] = post['id']
            
            # Извлечение текста публикации
            post_data['text'] = post['text'].replace('\n', ' ') if 'text' in post else ''
            
            # Извлечение изображения под постом
            attachments = post.get('attachments', [])
            image_url = next((att['photo']['sizes'][-1]['url'] for att in attachments 
                              if att.get('type') == 'photo'), '')
            post_data['image_url'] = image_url
            
            # Извлечение количества просмотров
            views_count = post.get('views', {}).get('count', 0)
            post_data['views_count'] = views_count
            
            scraped_data.append(post_data)
        
        return scraped_data
    
    except vk_api.exceptions.ApiError as e:
        print(f"Error accessing VK API: {e}")
        return []


def save_to_csv(data, file_name='vk_wall_posts.csv'):
    """
    Функция сохраняет данные в CSV-файл.
    
    """
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['post_id', 'text', 'image_url', 'views_count'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def describe_stats(df):
    """
    Функция описывает основные статистические показатели данных.
    
    """
    print("\nСтатистика:")
    print(f"Количество постов: {len(df)}")
    print(f"Среднее количество просмотров: {df['views_count'].mean():.2f}")
    print(f"Медиана количества просмотров: {df['views_count'].median():.2f}")
    print(f"Максимальное количество просмотров: {df['views_count'].max()}")
    print(f"Пост с максимальным количеством просмотров:\n{df.iloc[df['views_count'].argmax()]}\n")


def visualize_views(df):
    """
    Данная функция строит график распределения количества просмотров.
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x="views_count", bins=20)
    plt.title("Распределение количества просмотров")
    plt.xlabel("Количество просмотров")
    plt.ylabel("Частота")
    plt.show()


def main():
    token = 'vk1.a.TQUeeru5OR1rXad_EfV-hPYJhxsbnvw_JtyaWzjIxNaGJekLxEOPLPGuOPS6xL7Zd09hw1-dldW5PDJpYFPNA3_S6E7J8xZjWjdPMVUgc_YQ-y-XsLTBBFuUdsQeCi_yEVsTxUmI_MH1yE3OvySbu7gKEInsGNbWrO50xAo2iaMCMeWkoTpjS3Py6NwiQsRM5MbT4QQUArTtibu3erpIjA'
    owner_id = -152141431
    num_posts = 50 
    wall_data = scrape_wall_data(token, owner_id, num_posts)
    
    if wall_data:
        df = pd.DataFrame(wall_data)  
        save_to_csv(wall_data)
        describe_stats(df)
        visualize_views(df)
    else:
        print("Нет данных.")


if __name__ == "__main__":
    main()