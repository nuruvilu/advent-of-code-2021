(require '[clojure.string :as string])
(require '[clojure.math.combinatorics :as combo])

(def hypernet-regex #"\[[^(\[|\])]+\]")

(defn abba? [[a b c d]] (and (not= a b) (= [a b] [d c])))

(defn aba? [[a b c]] (and (not= a b) (= a c)))

(defn aba&bab? [[a1 b1 _] [a2 b2 _]] (abba? [a1 b1 a2 b2]))

(defn scroll [lst times]
  (loop [l lst t (dec times) acc [lst]]
    (if (<= t 0)
      (apply map vector acc)
      (recur (rest l) (dec t) (conj acc (rest l))))))

(defn get-abas [ss] (mapcat #(filter aba? (scroll % 3)) ss))

(defn contains-abba? [s]
  (and (>= (count s) 4)
       (boolean (seq (filter abba? (scroll s 4))))))

(defn get-hypernets [ip] (re-seq hypernet-regex ip))

(defn supports-tls? [ip]
  (and (empty? (filter contains-abba? (get-hypernets ip)))
       (contains-abba? ip)))

(defn supports-ssl? [ip]
  (let [abas (get-abas (string/split ip hypernet-regex))
        babs (get-abas (get-hypernets ip))]
    (boolean (seq (filter #(apply aba&bab? %)
                          (combo/cartesian-product abas babs))))))

(defn part1 [input] (count (filter supports-tls? (string/split-lines input))))

(defn part2 [input] (count (filter supports-ssl? (string/split-lines input))))

(def sample1 (slurp "../samples/day07-1.txt"))
(assert (= (part1 sample1) 2))
(def sample2 (slurp "../samples/day07-2.txt"))
(assert (= (part2 sample2) 3))

(def input (slurp "../inputs/day07.txt"))
(println {:silver (part1 input) :gold (part2 input)})
