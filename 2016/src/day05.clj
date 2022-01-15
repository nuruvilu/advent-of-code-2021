(import java.security.MessageDigest
        java.math.BigInteger)
(require '[clojure.string :as string])

(defn md5 [string]
  (format "%032x"
          (BigInteger. 1 (.digest (MessageDigest/getInstance "MD5")
                                  (.getBytes string)))))

(defn find-password [input insert-char]
  (loop [i 0
         password (apply sorted-map (mapcat vector (range 8) (repeat nil)))
         filled 0]
    (if (>= filled 8)
      (apply str (vals password))
      (let [hash (md5 (str input i))]
        (if (string/starts-with? hash "00000")
          (let [new-password (insert-char password hash)]
            (recur (inc i)
                   new-password
                   (if (= password new-password) filled (inc filled))))
          (recur (inc i) password filled))))))

(defn part1 [input]
  (find-password input
                 (fn [pw hash]
                   (assoc pw (apply min (keys (filter #(= (% 1) nil) pw)))
                           (nth hash 5)))))

(defn part2 [input]
  (find-password input
                 (fn [pw hash]
                   (let [i-str (str (nth hash 5))]
                     (if (re-matches #"[0-7]" i-str)
                       (let [i (Integer/parseInt i-str)]
                         (if (= (pw i) nil) (assoc pw i (nth hash 6)) pw))
                       pw)))))

(def sample "abc")
(assert (= (part1 sample) "18f47a30"))
(assert (= (part2 sample) "05ace8e3"))

(def input "ffykfhsq")
(println {:silver (part1 input) :gold (part2 input)})
