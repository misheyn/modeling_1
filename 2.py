import random as rn

"""
 Задание обрабатывают последовательно два компьютера, максимальная очередь перед первым – 2
  (третья заявка получает отказ в обслуживании), перед вторым – не ог-раничена
"""
# INPUT
A1 = 1
A2 = 13
# PROCESSING
B1 = 1
B2 = 15

BLOCK = 3


def start():
    i, k = 0, 0
    t_input = 0  # момент поступления очередного задания
    t_wait = 0  # время ожидания задания в очереди
    t_pc1_wait = 0  # время простоя пк1
    t_pc2_wait = 0  # время простоя пк2
    t_pc1_end = 0  # момент окончания обработки очередного задания пк1
    t_pc2_end = 0  # момент окончания обработки очередного задания пк2
    queue_pc1 = 0
    t_wait_sum = 0
    t_pc1_wait_sum = 0
    t_pc2_wait_sum = 0
    t_being_sum = 0

    while i < 1000 and k < 1000:
        wait_input = rn.randint(A1, A2)  # интервал между поступлением заданий
        t_input = t_input + wait_input
        t_wait_process = rn.randint(B1, B2)  # интервал обработки задания
        if queue_pc1 < BLOCK:
            if t_input < t_pc1_end:
                queue_pc1 += 1
                t_wait += t_pc1_end - t_input
                # print(t_wait, "\n")
                t_wait_sum += t_wait
                t_pc1_end += t_wait_process
            else:
                k += 1
                if queue_pc1 != 0:
                    queue_pc1 -= 1
                t_pc1_wait += t_input - t_pc1_end
                t_pc1_wait_sum += t_pc1_wait
                t_pc1_end = t_input + t_wait_process
            t_being_sum += (t_pc1_end - t_input)
        else:
            if t_input < t_pc2_end:
                t_wait += t_pc2_end - t_input
                # print(t_wait, "\n")
                t_wait_sum += t_wait
                t_pc2_end += t_wait_process
            else:
                k += 1
                t_pc2_wait += t_input - t_pc2_end
                t_pc2_wait_sum += t_pc2_wait
                t_pc2_end = t_input + t_wait_process
            t_being_sum += (t_pc2_end - t_input)
        i += 1

    t_pc_wait = t_pc1_wait_sum + t_pc2_wait_sum
    p_pc1 = t_pc1_wait_sum / t_pc_wait * 100
    p_pc2 = t_pc2_wait_sum / t_pc_wait * 100
    return t_wait_sum, p_pc1, p_pc2, t_being_sum


f_av_wait, f_p_pc1, f_p_pc2, f_av_stay = 0, 0, 0, 0
for j in range(100):
    t_wait_sum, p_wait_pc1, p_wait_pc2, t_stay = start()
    f_av_wait += (t_wait_sum / 1000)
    f_p_pc1 += p_wait_pc1
    f_p_pc2 += p_wait_pc2
    f_av_stay += (t_stay / 1000)
    # print("Среднее время ожидания задания в очереди:", t_wait_sum / 1000)
    # print("Среднее время пребывания задания в системе: ", t_stay / 1000)
    # print("Вероятность простоя 1 пк: %.3f" % p_wait_pc1)
    # print("Вероятность простоя 2 пк: %.3f" % p_wait_pc2)

print("Среднее время ожидания задания в очереди: %.4f" % (f_av_wait / 100))
print("Среднее время пребывания задания в системе (в секундах): %.3f" % (f_av_stay / 100))
print("Вероятность простоя 1 пк: %.3f" % (f_p_pc1 / 100))
print("Вероятность простоя 2 пк: %.3f" % (f_p_pc2 / 100))
