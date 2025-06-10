from fastapi import FastAPI
import uvicorn
import math
import mmh3  # Для хеширования

class BloomFilter:
    def __init__(self, capacity: int, error_rate: float):
        """
        capacity: ожидаемое количество элементов
        error_rate: допустимая вероятность ложноположительных срабатываний
        """
        self.capacity = capacity
        self.error_rate = error_rate
        self.size = self.calculate_size(capacity, error_rate)
        self.hash_count = self.calculate_hash_count(self.size, capacity)
        self.bit_array = [False] * self.size

    @staticmethod
    def calculate_size(n, p):
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @staticmethod
    def calculate_hash_count(m, n):
        k = (m / n) * math.log(2)
        return int(k)

    def add(self, item: str):
        """Добавить элемент в фильтр"""
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = True

    def check(self, item: str) -> bool:
        """Проверить наличие элемента в фильтре"""
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            if not self.bit_array[index]:
                return False
        return True

app = FastAPI()

# Инициализируем фильтр Блума на 1000 элементов с вероятностью ошибки 1%
bloom_filter = BloomFilter(1000, 0.01)

@app.get("/")
async def root():
    return {"message": "Bloom Filter API", "status": "running"}

@app.get("/add/{item}")
async def add_item(item: str):
    """Добавить элемент в фильтр"""
    bloom_filter.add(item)
    return {"action": "added", "item": item}

@app.get("/check/{item}")
async def check_item(item: str):
    """Проверить элемент"""
    exists = bloom_filter.check(item)
    return {"item": item, "exists": exists}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)