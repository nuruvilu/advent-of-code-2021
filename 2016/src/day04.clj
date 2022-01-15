(require '[clojure.string :as string])

(defn make-chk-compare [freqs]
  (fn [k1 k2]
    (if (= (freqs k1) (freqs k2))
      (compare k1 k2)
      (compare (freqs k2) (freqs k1)))))

(defn calc-checksum [name]
  (let [freqs (frequencies (filter #(not= \- %) name))]
    (apply str (take 5 (keys (into (sorted-map-by (make-chk-compare freqs))
                                   freqs))))))

(defn real-room? [[name _ checksum]] (= (calc-checksum name) checksum))

(defn shift [c n]
  (if (= c \-)
    \space
    (char (+ (mod (+ (- (int c) 97) n) 26) 97))))

(defn decrypt [[name sector-id _]]
  (apply str (map shift name (repeat sector-id))))

(defn parse-room [room-text]
  (let [[lhs rhs] (string/split room-text #"\[")]
    [((re-find #"([a-z]|-)+[a-z]" lhs) 0)
     (Integer/parseInt (re-find #"[0-9]+" lhs))
     (subs rhs 0 (dec (count rhs)))]))

(defn parse [input-text] (map parse-room (string/split-lines input-text)))

(defn part1 [input]
  (->> (parse input)
       (filter real-room?)
       (map #(% 1))
       (reduce +)))

(defn part2 [input]
  ((first (->> (parse input)
               (filter real-room?)
               (filter #(string/includes? (decrypt %) "north")))) 1))

(def sample (slurp "../samples/day04.txt"))
(assert (= (calc-checksum "aaaaa-bbb-z-y-x") "abxyz"))
(assert (= (calc-checksum "a-b-c-d-e-f-g-h") "abcde"))
(assert (= (part1 sample) 1514))
(assert (= (decrypt ["qzmt-zixmtkozy-ivhz" 343 nil]) "very encrypted name"))

(def input (slurp "../inputs/day04.txt"))
(println {:silver (part1 input) :gold (part2 input)})
