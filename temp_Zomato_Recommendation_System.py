{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(51717, 17)"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df=pd.read_csv(\"zomato.csv\")\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.drop([\"reviews_list\"], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>url</th>\n",
       "      <th>address</th>\n",
       "      <th>name</th>\n",
       "      <th>online_order</th>\n",
       "      <th>book_table</th>\n",
       "      <th>rate</th>\n",
       "      <th>votes</th>\n",
       "      <th>phone</th>\n",
       "      <th>location</th>\n",
       "      <th>rest_type</th>\n",
       "      <th>dish_liked</th>\n",
       "      <th>cuisines</th>\n",
       "      <th>approx_cost(for two people)</th>\n",
       "      <th>menu_item</th>\n",
       "      <th>listed_in(type)</th>\n",
       "      <th>listed_in(city)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://www.zomato.com/bangalore/jalsa-banasha...</td>\n",
       "      <td>942, 21st Main Road, 2nd Stage, Banashankari, ...</td>\n",
       "      <td>Jalsa</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>4.1/5</td>\n",
       "      <td>775</td>\n",
       "      <td>080 42297555  +91 9743772233</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Pasta, Lunch Buffet, Masala Papad, Paneer Laja...</td>\n",
       "      <td>North Indian, Mughlai, Chinese</td>\n",
       "      <td>800</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://www.zomato.com/bangalore/spice-elephan...</td>\n",
       "      <td>2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...</td>\n",
       "      <td>Spice Elephant</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>4.1/5</td>\n",
       "      <td>787</td>\n",
       "      <td>080 41714161</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Momos, Lunch Buffet, Chocolate Nirvana, Thai G...</td>\n",
       "      <td>Chinese, North Indian, Thai</td>\n",
       "      <td>800</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://www.zomato.com/SanchurroBangalore?cont...</td>\n",
       "      <td>1112, Next to KIMS Medical College, 17th Cross...</td>\n",
       "      <td>San Churro Cafe</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8/5</td>\n",
       "      <td>918</td>\n",
       "      <td>+91 9663487993</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Cafe, Casual Dining</td>\n",
       "      <td>Churros, Cannelloni, Minestrone Soup, Hot Choc...</td>\n",
       "      <td>Cafe, Mexican, Italian</td>\n",
       "      <td>800</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://www.zomato.com/bangalore/addhuri-udupi...</td>\n",
       "      <td>1st Floor, Annakuteera, 3rd Stage, Banashankar...</td>\n",
       "      <td>Addhuri Udupi Bhojana</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.7/5</td>\n",
       "      <td>88</td>\n",
       "      <td>+91 9620009302</td>\n",
       "      <td>Banashankari</td>\n",
       "      <td>Quick Bites</td>\n",
       "      <td>Masala Dosa</td>\n",
       "      <td>South Indian, North Indian</td>\n",
       "      <td>300</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://www.zomato.com/bangalore/grand-village...</td>\n",
       "      <td>10, 3rd Floor, Lakshmi Associates, Gandhi Baza...</td>\n",
       "      <td>Grand Village</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>3.8/5</td>\n",
       "      <td>166</td>\n",
       "      <td>+91 8026612447  +91 9901210005</td>\n",
       "      <td>Basavanagudi</td>\n",
       "      <td>Casual Dining</td>\n",
       "      <td>Panipuri, Gol Gappe</td>\n",
       "      <td>North Indian, Rajasthani</td>\n",
       "      <td>600</td>\n",
       "      <td>[]</td>\n",
       "      <td>Buffet</td>\n",
       "      <td>Banashankari</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 url  \\\n",
       "0  https://www.zomato.com/bangalore/jalsa-banasha...   \n",
       "1  https://www.zomato.com/bangalore/spice-elephan...   \n",
       "2  https://www.zomato.com/SanchurroBangalore?cont...   \n",
       "3  https://www.zomato.com/bangalore/addhuri-udupi...   \n",
       "4  https://www.zomato.com/bangalore/grand-village...   \n",
       "\n",
       "                                             address                   name  \\\n",
       "0  942, 21st Main Road, 2nd Stage, Banashankari, ...                  Jalsa   \n",
       "1  2nd Floor, 80 Feet Road, Near Big Bazaar, 6th ...         Spice Elephant   \n",
       "2  1112, Next to KIMS Medical College, 17th Cross...        San Churro Cafe   \n",
       "3  1st Floor, Annakuteera, 3rd Stage, Banashankar...  Addhuri Udupi Bhojana   \n",
       "4  10, 3rd Floor, Lakshmi Associates, Gandhi Baza...          Grand Village   \n",
       "\n",
       "  online_order book_table   rate  votes                           phone  \\\n",
       "0          Yes        Yes  4.1/5    775    080 42297555  +91 9743772233   \n",
       "1          Yes         No  4.1/5    787                    080 41714161   \n",
       "2          Yes         No  3.8/5    918                  +91 9663487993   \n",
       "3           No         No  3.7/5     88                  +91 9620009302   \n",
       "4           No         No  3.8/5    166  +91 8026612447  +91 9901210005   \n",
       "\n",
       "       location            rest_type  \\\n",
       "0  Banashankari        Casual Dining   \n",
       "1  Banashankari        Casual Dining   \n",
       "2  Banashankari  Cafe, Casual Dining   \n",
       "3  Banashankari          Quick Bites   \n",
       "4  Basavanagudi        Casual Dining   \n",
       "\n",
       "                                          dish_liked  \\\n",
       "0  Pasta, Lunch Buffet, Masala Papad, Paneer Laja...   \n",
       "1  Momos, Lunch Buffet, Chocolate Nirvana, Thai G...   \n",
       "2  Churros, Cannelloni, Minestrone Soup, Hot Choc...   \n",
       "3                                        Masala Dosa   \n",
       "4                                Panipuri, Gol Gappe   \n",
       "\n",
       "                         cuisines approx_cost(for two people) menu_item  \\\n",
       "0  North Indian, Mughlai, Chinese                         800        []   \n",
       "1     Chinese, North Indian, Thai                         800        []   \n",
       "2          Cafe, Mexican, Italian                         800        []   \n",
       "3      South Indian, North Indian                         300        []   \n",
       "4        North Indian, Rajasthani                         600        []   \n",
       "\n",
       "  listed_in(type) listed_in(city)  \n",
       "0          Buffet    Banashankari  \n",
       "1          Buffet    Banashankari  \n",
       "2          Buffet    Banashankari  \n",
       "3          Buffet    Banashankari  \n",
       "4          Buffet    Banashankari  "
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.map(lambda x: x.replace('\\n', ' ') if isinstance(x, str) else x)\n",
    "df = df.replace('\\r', ' ', regex=True)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(\"zomato_new.csv\",index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyspark.sql import SparkSession\n",
    "spark = SparkSession.builder.appName(\"Recommendation System\").config(\"spark.driver.memory\", \"8g\").config(\"spark.executor.memory\", \"8g\") \\\n",
    "    .config(\"spark.executor.cores\", \"8\") \\\n",
    "    .getOrCreate()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---+-------+----+------------+----------+----+-----+-----+--------+---------+----------+--------+---------------------------+---------+---------------+---------------+\n",
      "|url|address|name|online_order|book_table|rate|votes|phone|location|rest_type|dish_liked|cuisines|approx_cost(for two people)|menu_item|listed_in(type)|listed_in(city)|\n",
      "+---+-------+----+------------+----------+----+-----+-----+--------+---------+----------+--------+---------------------------+---------+---------------+---------------+\n",
      "|  0|      0|   0|           0|         0|7775|    0| 1208|      21|      227|     28078|      45|                        346|        0|              0|              0|\n",
      "+---+-------+----+------------+----------+----+-----+-----+--------+---------+----------+--------+---------------------------+---------+---------------+---------------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from pyspark.sql.functions import col, regexp_replace,regexp_extract\n",
    "from pyspark.sql.functions import col, avg, when, coalesce,split,count\n",
    "df=spark.read.csv(\"zomato_new.csv\",header=True,inferSchema=True)\n",
    "null_counts = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])\n",
    "null_counts.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+------------+----------+-----+------------+--------------------+---------------------------+---------------+\n",
      "|                name|online_order|book_table| rate|    location|            cuisines|approx_cost(for two people)|listed_in(type)|\n",
      "+--------------------+------------+----------+-----+------------+--------------------+---------------------------+---------------+\n",
      "|               Jalsa|         Yes|       Yes|4.1/5|Banashankari|North Indian, Mug...|                        800|         Buffet|\n",
      "|      Spice Elephant|         Yes|        No|4.1/5|Banashankari|Chinese, North In...|                        800|         Buffet|\n",
      "|     San Churro Cafe|         Yes|        No|3.8/5|Banashankari|Cafe, Mexican, It...|                        800|         Buffet|\n",
      "|Addhuri Udupi Bho...|          No|        No|3.7/5|Banashankari|South Indian, Nor...|                        300|         Buffet|\n",
      "|       Grand Village|          No|        No|3.8/5|Basavanagudi|North Indian, Raj...|                        600|         Buffet|\n",
      "|     Timepass Dinner|         Yes|        No|3.8/5|Basavanagudi|        North Indian|                        600|         Buffet|\n",
      "|Rosewood Internat...|          No|        No|3.6/5| Mysore Road|North Indian, Sou...|                        800|         Buffet|\n",
      "|              Onesta|         Yes|       Yes|4.6/5|Banashankari|Pizza, Cafe, Italian|                        600|          Cafes|\n",
      "|      Penthouse Cafe|         Yes|        No|4.0/5|Banashankari|Cafe, Italian, Co...|                        700|          Cafes|\n",
      "|           Smacznego|         Yes|        No|4.2/5|Banashankari|Cafe, Mexican, It...|                        550|          Cafes|\n",
      "|CafÃÂÃÂÃÂÃ...|         Yes|        No|4.1/5|Banashankari|                Cafe|                        500|          Cafes|\n",
      "|        Cafe Shuffle|         Yes|       Yes|4.2/5|Banashankari|Cafe, Italian, Co...|                        600|          Cafes|\n",
      "|    The Coffee Shack|         Yes|       Yes|4.2/5|Banashankari|Cafe, Chinese, Co...|                        500|          Cafes|\n",
      "|          Caf-Eleven|          No|        No|4.0/5|Banashankari|   Cafe, Continental|                        450|          Cafes|\n",
      "|     San Churro Cafe|         Yes|        No|3.8/5|Banashankari|Cafe, Mexican, It...|                        800|          Cafes|\n",
      "|       Cafe Vivacity|         Yes|        No|3.8/5|Banashankari|                Cafe|                        650|          Cafes|\n",
      "|        Catch-up-ino|         Yes|        No|3.9/5|Banashankari|Cafe, Fast Food, ...|                        800|          Cafes|\n",
      "|    Kirthi's Biryani|         Yes|        No|3.8/5|Banashankari|Chinese, Cafe, It...|                        700|          Cafes|\n",
      "|            T3H Cafe|          No|        No|3.9/5|Banashankari|Cafe, Italian, Am...|                        300|          Cafes|\n",
      "|360 Atoms Restaur...|         Yes|        No|3.1/5|Banashankari|Cafe, Chinese, Co...|                        400|          Cafes|\n",
      "+--------------------+------------+----------+-----+------------+--------------------+---------------------------+---------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df = df.drop(\"url\",\"phone\",'address',\"rest_type\",\"dish_liked\",\"listed_in(city)\", 'menu_item', 'votes')\n",
    "df.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+\n",
      "|            cuisines|\n",
      "+--------------------+\n",
      "|[Andhra,  South I...|\n",
      "|[South Indian,  N...|\n",
      "|[Lebanese,  Medit...|\n",
      "|[Bengali,  North ...|\n",
      "|[North Indian,  B...|\n",
      "|[South Indian,  C...|\n",
      "|[Desserts,  Bever...|\n",
      "|[Chinese,  South ...|\n",
      "|[Chinese,  South ...|\n",
      "|[Fast Food,  Arab...|\n",
      "|[Cafe,  Italian, ...|\n",
      "|[North Indian,  C...|\n",
      "|[American,  Sandw...|\n",
      "|[Rajasthani,  Nor...|\n",
      "|[Continental,  Ch...|\n",
      "|[Chinese,  Seafoo...|\n",
      "|[Arabian,  Middle...|\n",
      "|[Chinese,  Fast F...|\n",
      "|[Seafood,  Biryan...|\n",
      "|[Mughlai,  North ...|\n",
      "+--------------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df=df.withColumn(\"cuisines\", split(df[\"cuisines\"], \",\"))\n",
    "df.select(\"cuisines\").distinct().show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----+\n",
      "|rate|\n",
      "+----+\n",
      "| 2.5|\n",
      "| 3.8|\n",
      "| 2.2|\n",
      "| 4.6|\n",
      "| 3.4|\n",
      "| 4.2|\n",
      "| 3.2|\n",
      "| 3.6|\n",
      "| 3.0|\n",
      "| 2.9|\n",
      "|NULL|\n",
      "| 2.6|\n",
      "| 3.3|\n",
      "| 2.8|\n",
      "| 4.4|\n",
      "| 3.5|\n",
      "| 4.1|\n",
      "| 4.8|\n",
      "| 2.4|\n",
      "| 2.7|\n",
      "+----+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df = df.withColumn(\"rate\", regexp_extract(col(\"rate\"), r\"(\\d+\\.?\\d*)\", 0).cast(\"float\"))\n",
    "# df = df.filter((col(\"rate\") != \"NEW\") & (col(\"rate\") != \"-\"))\n",
    "df.select(\"rate\").distinct().show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+------------+----------+----+------------+--------------------+----+------+\n",
      "|                name|online_order|book_table|rate|    location|            cuisines|cost|  type|\n",
      "+--------------------+------------+----------+----+------------+--------------------+----+------+\n",
      "|               Jalsa|         Yes|       Yes| 4.1|Banashankari|[North Indian,  M...| 800|Buffet|\n",
      "|      Spice Elephant|         Yes|        No| 4.1|Banashankari|[Chinese,  North ...| 800|Buffet|\n",
      "|     San Churro Cafe|         Yes|        No| 3.8|Banashankari|[Cafe,  Mexican, ...| 800|Buffet|\n",
      "|Addhuri Udupi Bho...|          No|        No| 3.7|Banashankari|[South Indian,  N...| 300|Buffet|\n",
      "|       Grand Village|          No|        No| 3.8|Basavanagudi|[North Indian,  R...| 600|Buffet|\n",
      "|     Timepass Dinner|         Yes|        No| 3.8|Basavanagudi|      [North Indian]| 600|Buffet|\n",
      "|Rosewood Internat...|          No|        No| 3.6| Mysore Road|[North Indian,  S...| 800|Buffet|\n",
      "|              Onesta|         Yes|       Yes| 4.6|Banashankari|[Pizza,  Cafe,  I...| 600| Cafes|\n",
      "|      Penthouse Cafe|         Yes|        No| 4.0|Banashankari|[Cafe,  Italian, ...| 700| Cafes|\n",
      "|           Smacznego|         Yes|        No| 4.2|Banashankari|[Cafe,  Mexican, ...| 550| Cafes|\n",
      "|CafÃÂÃÂÃÂÃ...|         Yes|        No| 4.1|Banashankari|              [Cafe]| 500| Cafes|\n",
      "|        Cafe Shuffle|         Yes|       Yes| 4.2|Banashankari|[Cafe,  Italian, ...| 600| Cafes|\n",
      "|    The Coffee Shack|         Yes|       Yes| 4.2|Banashankari|[Cafe,  Chinese, ...| 500| Cafes|\n",
      "|          Caf-Eleven|          No|        No| 4.0|Banashankari|[Cafe,  Continental]| 450| Cafes|\n",
      "|     San Churro Cafe|         Yes|        No| 3.8|Banashankari|[Cafe,  Mexican, ...| 800| Cafes|\n",
      "|       Cafe Vivacity|         Yes|        No| 3.8|Banashankari|              [Cafe]| 650| Cafes|\n",
      "|        Catch-up-ino|         Yes|        No| 3.9|Banashankari|[Cafe,  Fast Food...| 800| Cafes|\n",
      "|    Kirthi's Biryani|         Yes|        No| 3.8|Banashankari|[Chinese,  Cafe, ...| 700| Cafes|\n",
      "|            T3H Cafe|          No|        No| 3.9|Banashankari|[Cafe,  Italian, ...| 300| Cafes|\n",
      "|360 Atoms Restaur...|         Yes|        No| 3.1|Banashankari|[Cafe,  Chinese, ...| 400| Cafes|\n",
      "+--------------------+------------+----------+----+------------+--------------------+----+------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df = (df\n",
    "          .withColumnRenamed(\"approx_cost(for two people)\", \"cost\")\n",
    "          .withColumnRenamed(\"listed_in(type)\", \"type\"))\n",
    "df.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-----+\n",
      "| cost|\n",
      "+-----+\n",
      "|550.0|\n",
      "|500.0|\n",
      "|190.0|\n",
      "|350.0|\n",
      "|700.0|\n",
      "|650.0|\n",
      "|750.0|\n",
      "|850.0|\n",
      "|180.0|\n",
      "|100.0|\n",
      "| NULL|\n",
      "| 40.0|\n",
      "|250.0|\n",
      "|400.0|\n",
      "|200.0|\n",
      "| 50.0|\n",
      "| 80.0|\n",
      "|150.0|\n",
      "|450.0|\n",
      "|800.0|\n",
      "+-----+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df = df.withColumn(\"cost\", round(col(\"cost\").cast(\"float\"),2))\n",
    "df.select(\"cost\").distinct().show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "|    location|                name|online_order|book_table|rate|            cuisines| cost|  type|\n",
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "|Banashankari|               Jalsa|         Yes|       Yes| 4.1|[North Indian,  M...|800.0|Buffet|\n",
      "|Banashankari|      Spice Elephant|         Yes|        No| 4.1|[Chinese,  North ...|800.0|Buffet|\n",
      "|Banashankari|     San Churro Cafe|         Yes|        No| 3.8|[Cafe,  Mexican, ...|800.0|Buffet|\n",
      "|Banashankari|Addhuri Udupi Bho...|          No|        No| 3.7|[South Indian,  N...|300.0|Buffet|\n",
      "|Basavanagudi|       Grand Village|          No|        No| 3.8|[North Indian,  R...|600.0|Buffet|\n",
      "|Basavanagudi|     Timepass Dinner|         Yes|        No| 3.8|      [North Indian]|600.0|Buffet|\n",
      "| Mysore Road|Rosewood Internat...|          No|        No| 3.6|[North Indian,  S...|800.0|Buffet|\n",
      "|Banashankari|              Onesta|         Yes|       Yes| 4.6|[Pizza,  Cafe,  I...|600.0| Cafes|\n",
      "|Banashankari|      Penthouse Cafe|         Yes|        No| 4.0|[Cafe,  Italian, ...|700.0| Cafes|\n",
      "|Banashankari|           Smacznego|         Yes|        No| 4.2|[Cafe,  Mexican, ...|550.0| Cafes|\n",
      "|Banashankari|CafÃÂÃÂÃÂÃ...|         Yes|        No| 4.1|              [Cafe]|500.0| Cafes|\n",
      "|Banashankari|        Cafe Shuffle|         Yes|       Yes| 4.2|[Cafe,  Italian, ...|600.0| Cafes|\n",
      "|Banashankari|    The Coffee Shack|         Yes|       Yes| 4.2|[Cafe,  Chinese, ...|500.0| Cafes|\n",
      "|Banashankari|          Caf-Eleven|          No|        No| 4.0|[Cafe,  Continental]|450.0| Cafes|\n",
      "|Banashankari|     San Churro Cafe|         Yes|        No| 3.8|[Cafe,  Mexican, ...|800.0| Cafes|\n",
      "|Banashankari|       Cafe Vivacity|         Yes|        No| 3.8|              [Cafe]|650.0| Cafes|\n",
      "|Banashankari|        Catch-up-ino|         Yes|        No| 3.9|[Cafe,  Fast Food...|800.0| Cafes|\n",
      "|Banashankari|    Kirthi's Biryani|         Yes|        No| 3.8|[Chinese,  Cafe, ...|700.0| Cafes|\n",
      "|Banashankari|            T3H Cafe|          No|        No| 3.9|[Cafe,  Italian, ...|300.0| Cafes|\n",
      "|Banashankari|360 Atoms Restaur...|         Yes|        No| 3.1|[Cafe,  Chinese, ...|400.0| Cafes|\n",
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "avg_cost_per_restaurant = df.groupBy(\"location\").agg(avg(\"cost\").alias(\"Avg Cost\"))\n",
    "\n",
    "df = df.join(avg_cost_per_restaurant, on=\"location\", how=\"left\")\n",
    "\n",
    "df= df.withColumn(\"cost\", coalesce(col(\"cost\"), col(\"Avg Cost\")))\n",
    "\n",
    "df = df.drop(\"Avg Cost\")\n",
    "\n",
    "df.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "|    location|                name|online_order|book_table|rate|            cuisines| cost|  type|\n",
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "|Banashankari|               Jalsa|         Yes|       Yes| 4.1|[North Indian,  M...|800.0|Buffet|\n",
      "|Banashankari|      Spice Elephant|         Yes|        No| 4.1|[Chinese,  North ...|800.0|Buffet|\n",
      "|Banashankari|     San Churro Cafe|         Yes|        No| 3.8|[Cafe,  Mexican, ...|800.0|Buffet|\n",
      "|Banashankari|Addhuri Udupi Bho...|          No|        No| 3.7|[South Indian,  N...|300.0|Buffet|\n",
      "|Basavanagudi|       Grand Village|          No|        No| 3.8|[North Indian,  R...|600.0|Buffet|\n",
      "|Basavanagudi|     Timepass Dinner|         Yes|        No| 3.8|      [North Indian]|600.0|Buffet|\n",
      "| Mysore Road|Rosewood Internat...|          No|        No| 3.6|[North Indian,  S...|800.0|Buffet|\n",
      "|Banashankari|              Onesta|         Yes|       Yes| 4.6|[Pizza,  Cafe,  I...|600.0| Cafes|\n",
      "|Banashankari|      Penthouse Cafe|         Yes|        No| 4.0|[Cafe,  Italian, ...|700.0| Cafes|\n",
      "|Banashankari|           Smacznego|         Yes|        No| 4.2|[Cafe,  Mexican, ...|550.0| Cafes|\n",
      "|Banashankari|CafÃÂÃÂÃÂÃ...|         Yes|        No| 4.1|              [Cafe]|500.0| Cafes|\n",
      "|Banashankari|        Cafe Shuffle|         Yes|       Yes| 4.2|[Cafe,  Italian, ...|600.0| Cafes|\n",
      "|Banashankari|    The Coffee Shack|         Yes|       Yes| 4.2|[Cafe,  Chinese, ...|500.0| Cafes|\n",
      "|Banashankari|          Caf-Eleven|          No|        No| 4.0|[Cafe,  Continental]|450.0| Cafes|\n",
      "|Banashankari|     San Churro Cafe|         Yes|        No| 3.8|[Cafe,  Mexican, ...|800.0| Cafes|\n",
      "|Banashankari|       Cafe Vivacity|         Yes|        No| 3.8|              [Cafe]|650.0| Cafes|\n",
      "|Banashankari|        Catch-up-ino|         Yes|        No| 3.9|[Cafe,  Fast Food...|800.0| Cafes|\n",
      "|Banashankari|    Kirthi's Biryani|         Yes|        No| 3.8|[Chinese,  Cafe, ...|700.0| Cafes|\n",
      "|Banashankari|            T3H Cafe|          No|        No| 3.9|[Cafe,  Italian, ...|300.0| Cafes|\n",
      "|Banashankari|360 Atoms Restaur...|         Yes|        No| 3.1|[Cafe,  Chinese, ...|400.0| Cafes|\n",
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "avg_rating_per_location = df.groupBy(\"location\").agg(avg(\"rate\").alias(\"Location Avg Rating\"))\n",
    "\n",
    "df = df.join(avg_rating_per_location, on=\"location\", how=\"left\")\n",
    "\n",
    "df = df.withColumn(\"rate\", coalesce(col(\"rate\"), col(\"Location Avg Rating\")))\n",
    "\n",
    "df = df.drop(\"Location Avg Rating\")\n",
    "\n",
    "df = df.withColumn(\"rate\", round(col(\"rate\"), 2))\n",
    "\n",
    "df.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------+----+------------+----------+----+--------+----+----+\n",
      "|location|name|online_order|book_table|rate|cuisines|cost|type|\n",
      "+--------+----+------------+----------+----+--------+----+----+\n",
      "|      21|   0|           0|         0|  29|      45|  26|   0|\n",
      "+--------+----+------------+----------+----+--------+----+----+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "null_counts = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])\n",
    "\n",
    "null_counts.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "|    location|                name|online_order|book_table|rate|            cuisines| cost|  type|\n",
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "|Banashankari|               Jalsa|         Yes|       Yes| 4.1|[North Indian,  M...|800.0|Buffet|\n",
      "|Banashankari|      Spice Elephant|         Yes|        No| 4.1|[Chinese,  North ...|800.0|Buffet|\n",
      "|Banashankari|     San Churro Cafe|         Yes|        No| 3.8|[Cafe,  Mexican, ...|800.0|Buffet|\n",
      "|Banashankari|Addhuri Udupi Bho...|          No|        No| 3.7|[South Indian,  N...|300.0|Buffet|\n",
      "|Basavanagudi|       Grand Village|          No|        No| 3.8|[North Indian,  R...|600.0|Buffet|\n",
      "|Basavanagudi|     Timepass Dinner|         Yes|        No| 3.8|      [North Indian]|600.0|Buffet|\n",
      "| Mysore Road|Rosewood Internat...|          No|        No| 3.6|[North Indian,  S...|800.0|Buffet|\n",
      "|Banashankari|              Onesta|         Yes|       Yes| 4.6|[Pizza,  Cafe,  I...|600.0| Cafes|\n",
      "|Banashankari|      Penthouse Cafe|         Yes|        No| 4.0|[Cafe,  Italian, ...|700.0| Cafes|\n",
      "|Banashankari|           Smacznego|         Yes|        No| 4.2|[Cafe,  Mexican, ...|550.0| Cafes|\n",
      "|Banashankari|CafÃÂÃÂÃÂÃ...|         Yes|        No| 4.1|              [Cafe]|500.0| Cafes|\n",
      "|Banashankari|        Cafe Shuffle|         Yes|       Yes| 4.2|[Cafe,  Italian, ...|600.0| Cafes|\n",
      "|Banashankari|    The Coffee Shack|         Yes|       Yes| 4.2|[Cafe,  Chinese, ...|500.0| Cafes|\n",
      "|Banashankari|          Caf-Eleven|          No|        No| 4.0|[Cafe,  Continental]|450.0| Cafes|\n",
      "|Banashankari|     San Churro Cafe|         Yes|        No| 3.8|[Cafe,  Mexican, ...|800.0| Cafes|\n",
      "|Banashankari|       Cafe Vivacity|         Yes|        No| 3.8|              [Cafe]|650.0| Cafes|\n",
      "|Banashankari|        Catch-up-ino|         Yes|        No| 3.9|[Cafe,  Fast Food...|800.0| Cafes|\n",
      "|Banashankari|    Kirthi's Biryani|         Yes|        No| 3.8|[Chinese,  Cafe, ...|700.0| Cafes|\n",
      "|Banashankari|            T3H Cafe|          No|        No| 3.9|[Cafe,  Italian, ...|300.0| Cafes|\n",
      "|Banashankari|360 Atoms Restaur...|         Yes|        No| 3.1|[Cafe,  Chinese, ...|400.0| Cafes|\n",
      "+------------+--------------------+------------+----------+----+--------------------+-----+------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df = df.na.drop(subset=[\"cost\",\"cuisines\",\"rate\"])\n",
    "\n",
    "df.show()\n",
    "df = df.dropDuplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------+----+------------+----------+----+--------+----+----+\n",
      "|location|name|online_order|book_table|rate|cuisines|cost|type|\n",
      "+--------+----+------------+----------+----+--------+----+----+\n",
      "|       0|   0|           0|         0|   0|       0|   0|   0|\n",
      "+--------+----+------------+----------+----+--------+----+----+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "null_counts = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])\n",
    "\n",
    "null_counts.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Kumaraswamy Layout', 'Jayanagar', 'Basavanagudi', 'Banashankari', 'Mysore Road', 'BTM', 'Bannerghatta Road', 'Marathahalli', 'HSR', 'Sarjapur Road', 'Bellandur', 'Brigade Road', 'JP Nagar', 'City Market', 'Vasanth Nagar', 'Richmond Road', 'MG Road', 'Indiranagar', 'Residency Road', 'Shanti Nagar', 'Ulsoor', 'Wilson Garden', 'Race Course Road', 'South Bangalore', 'Koramangala 5th Block', 'Domlur', 'Shivajinagar', 'Kanakapura Road', 'Frazer Town', 'Cunningham Road', 'Lavelle Road', 'Koramangala 7th Block', 'Church Street', 'Koramangala 8th Block', 'St. Marks Road', 'Infantry Road', 'Uttarahalli', 'Rajarajeshwari Nagar', 'Commercial Street', 'Jalahalli', 'Whitefield', 'Bommanahalli', 'Koramangala 6th Block', 'Brookefield', 'ITPL Main Road, Whitefield', 'Koramangala 2nd Block', 'Varthur Main Road, Whitefield', 'Majestic', 'Hosur Road', 'Koramangala 1st Block', 'Koramangala', 'Koramangala 4th Block', 'Koramangala 3rd Block', 'Sanjay Nagar', 'Ejipura', 'Electronic City', 'Kammanahalli', 'Banaswadi', 'Hennur', 'North Bangalore', 'RT Nagar', 'Nagawara', 'Jeevan Bhima Nagar', 'Old Airport Road', 'Thippasandra', 'CV Raman Nagar', 'Old Madras Road', 'Kaggadasapura', 'Rammurthy Nagar', 'East Bangalore', 'HBR Layout', 'Kalyan Nagar', 'Hebbal', 'Nagarbhavi', 'Rajajinagar', 'Malleshwaram', 'Basaveshwara Nagar', 'Sadashiv Nagar', 'Seshadripuram', 'New BEL Road', 'Yeshwantpur', 'Yelahanka', 'Sankey Road', 'Sahakara Nagar', 'Vijay Nagar', 'Magadi Road', 'West Bangalore', 'KR Puram', 'Langford Town', 'Central Bangalore', 'Kengeri', 'Peenya']\n"
     ]
    }
   ],
   "source": [
    "# Convert the PySpark DataFrame to a Pandas DataFrame\n",
    "pandas_df = df.select(\"location\").toPandas()\n",
    "\n",
    "# Get unique values from the 'location' column and convert to a Python list\n",
    "unique_locations = pandas_df[\"location\"].dropna().unique().tolist()\n",
    "\n",
    "# Print the unique locations\n",
    "print(unique_locations)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Goan', ' Seafood', ' North Indian', ' Chinese', ' Biryani', 'South Indian', 'Juices', 'Sandwich', ' Beverages', ' Street Food', 'North Indian', ' South Indian', ' Fast Food', 'Chinese', 'Desserts', ' Momos', 'Pizza', ' Italian', ' Thai', ' BBQ', 'Steak', ' Continental', ' Mughlai', ' Arabian', ' Kerala', 'Fast Food', 'American', ' Tex-Mex', ' Burger', 'Biryani', 'Mangalorean', 'Continental', ' Mexican', ' Steak', ' Bakery', ' Finger Food', 'Andhra', 'Bakery', ' Cafe', ' Coffee', ' Desserts', ' Sandwich', 'Italian', ' Rolls', 'Burger', ' American', ' Kebab', 'Street Food', ' French', 'Cafe', 'Seafood', 'Finger Food', 'Healthy Food', ' Juices', ' Tea', ' Mediterranean', ' Iranian', ' Andhra', 'Mithai', ' Pizza', 'Salad', 'Kerala', 'Beverages', 'Arabian', ' Ice Cream', 'Ice Cream', 'Tea', 'Thai', ' Vietnamese', 'Hyderabadi', 'BBQ', 'Mughlai', ' Salad', 'Bengali', ' Bihari', ' Lucknowi', 'Mexican', ' Tibetan', ' Afghani', 'Australian', ' Healthy Food', 'Mediterranean', ' European', ' Mithai', ' Asian', ' Hyderabadi', 'European', 'Tamil', ' Chettinad', ' Middle Eastern', 'Roast Chicken', ' Japanese', ' Kashmiri', 'Drinks Only', 'Momos', 'Maharashtrian', 'Rajasthani', ' Charcoal Chicken', 'Rolls', 'Asian', ' Lebanese', ' Mangalorean', ' Gujarati', ' Maharashtrian', ' Bengali', 'Tibetan', 'Chettinad', 'Konkan', ' Indonesian', 'Burmese', ' Bar Food', ' Konkan', 'Turkish', ' Oriya', 'Spanish', ' Spanish', 'Japanese', 'North Eastern', ' Naga', 'Oriya', 'Modern Indian', ' Wraps', 'Bihari', 'Lebanese', ' Grill', 'Parsi', ' Turkish', ' Malaysian', ' Korean', ' South American', 'French', 'Korean', ' Rajasthani', ' Singaporean', 'Malaysian', 'Kebab', ' Afghan', ' Bubble Tea', 'Awadhi', ' Greek', ' Modern Indian', ' North Eastern', ' Nepalese', ' Assamese', 'Middle Eastern', ' German', 'Portuguese', ' African', 'Russian', ' Paan', 'Bohri', 'Vietnamese', ' Goan', 'Bar Food', 'Iranian', 'Naga', 'Kashmiri', 'Assamese', ' Sushi', ' Sindhi', 'German', ' Burmese', ' Hot dogs', ' Sri Lankan', 'British', 'African', ' Indian', 'Nepalese', ' Belgian', ' Roast Chicken', 'Lucknowi', 'Coffee', ' Awadhi', 'Singaporean', ' British', ' Pan Asian', ' Jewish', ' Vegan', ' Raw Meats', 'Gujarati', 'South American', ' Mongolian', ' Parsi', 'Charcoal Chicken', 'Indonesian', 'Belgian', ' Malwani', 'Sushi', ' Drinks Only', ' Cantonese']\n",
      "190\n",
      "92\n"
     ]
    }
   ],
   "source": [
    "from pyspark.sql.functions import col, explode\n",
    "\n",
    "# Convert the Spark DataFrame to a Pandas DataFrame, flattening the array column\n",
    "pandas_df = df.select(explode(col(\"cuisines\")).alias(\"cuisine\")).toPandas()\n",
    "\n",
    "# Get unique values from the flattened column and convert to a Python list\n",
    "unique_cuisines = pandas_df[\"cuisine\"].dropna().unique().tolist()\n",
    "\n",
    "# Print the result\n",
    "print(unique_cuisines)\n",
    "print(len(unique_cuisines))\n",
    "print(len(unique_locations))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows: 24850, Columns: 8\n"
     ]
    }
   ],
   "source": [
    "num_rows = df.count()\n",
    "\n",
    "num_columns = len(df.columns)\n",
    "\n",
    "print(f\"Rows: {num_rows}, Columns: {num_columns}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# from distutils.version import LooseVersion\n",
    "from pyspark.ml.recommendation import ALS\n",
    "from pyspark.ml.feature import StringIndexer\n",
    "\n",
    "location_indexer = StringIndexer(inputCol=\"location\", outputCol=\"location_id\")\n",
    "name_indexer = StringIndexer(inputCol=\"name\", outputCol=\"name_id\")\n",
    "\n",
    "df = location_indexer.fit(df).transform(df)\n",
    "df = name_indexer.fit(df).transform(df)\n",
    "\n",
    "\n",
    "als = ALS(\n",
    "    maxIter=10,\n",
    "    regParam=0.1,\n",
    "    userCol=\"location_id\",\n",
    "    itemCol=\"name_id\",\n",
    "    ratingCol=\"rate\", \n",
    "    coldStartStrategy=\"drop\"\n",
    ")\n",
    "\n",
    "model = als.fit(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---------------+----------------------------------------+----------------+\n",
      "|location       |name                                    |predicted_rating|\n",
      "+---------------+----------------------------------------+----------------+\n",
      "|Yelahanka      |Cheta's Kitchen                         |3.825882        |\n",
      "|Yelahanka      |Red Chillies Curries Point              |3.5708234       |\n",
      "|Yelahanka      |Prashanth Naati Corner                  |3.4334838       |\n",
      "|Yelahanka      |Twist N Roll                            |3.3353841       |\n",
      "|Whitefield     |Punjab Grill                            |4.7580833       |\n",
      "|Whitefield     |Flechazo                                |4.739569        |\n",
      "|Whitefield     |AB's - Absolute Barbecues               |4.6934066       |\n",
      "|Whitefield     |You Mee                                 |4.589632        |\n",
      "|Vasanth Nagar  |Belgian Waffle Factory                  |4.750819        |\n",
      "|Ulsoor         |Republic Of Noodles - Lemon Tree Premier|4.403236        |\n",
      "|Ulsoor         |Barbeque Nation                         |4.3769774       |\n",
      "|St. Marks Road |MISU                                    |4.531326        |\n",
      "|St. Marks Road |Truffles                                |4.499952        |\n",
      "|St. Marks Road |Hard Rock Cafe                          |4.3974676       |\n",
      "|South Bangalore|Crepe Nation                            |3.7006106       |\n",
      "|South Bangalore|Belly Squad Food Truck                  |3.7006106       |\n",
      "|South Bangalore|Gourmet Food Truck                      |3.635687        |\n",
      "|Shivajinagar   |Indy's Comfort Food                     |3.9991844       |\n",
      "|Shivajinagar   |New Hilal Restaurant                    |3.9397943       |\n",
      "|Shivajinagar   |Tiger Trail - Ramada Hotel              |3.901643        |\n",
      "+---------------+----------------------------------------+----------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from pyspark.sql.functions import col, explode\n",
    "\n",
    "location_recommendations = model.recommendForAllUsers(5)\n",
    "\n",
    "exploded_recommendations = location_recommendations.withColumn(\"recommendation\", explode(col(\"recommendations\")))\n",
    "\n",
    "final_recommendations = exploded_recommendations.select(\n",
    "    col(\"location_id\"),\n",
    "    col(\"recommendation.name_id\").alias(\"name_id\"),\n",
    "    col(\"recommendation.rating\").alias(\"predicted_rating\")\n",
    ")\n",
    "\n",
    "result = final_recommendations.join(df, on=[\"location_id\", \"name_id\"], how=\"inner\") \\\n",
    "                             .select(\"location\", \"name\", \"predicted_rating\") \\\n",
    "                             .distinct()\n",
    "result.orderBy(\"location\", \"predicted_rating\", ascending=False).show(truncate=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------------+----+------------------------+-----+\n",
      "|name         |rate|cuisines                |cost |\n",
      "+-------------+----+------------------------+-----+\n",
      "|Taaza Thindi |4.7 |[South Indian]          |100.0|\n",
      "|Onesta       |4.6 |[Pizza,  Cafe,  Italian]|600.0|\n",
      "|Onesta       |4.6 |[Pizza,  Cafe,  Italian]|600.0|\n",
      "|Onesta       |4.6 |[Pizza,  Cafe,  Italian]|600.0|\n",
      "|Poonam Sweets|4.4 |[Mithai]                |150.0|\n",
      "+-------------+----+------------------------+-----+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "input_location = \"Banashankari\"\n",
    "\n",
    "filtered_recommendations = df.filter(col(\"location\") == input_location) \\\n",
    "    .select(\"name\", \"rate\", \"cuisines\", \"cost\") \\\n",
    "    .orderBy(col(\"rate\").desc())\n",
    "filtered_recommendations.show(5, truncate=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---------------+----+------------+------------------+\n",
      "|name           |rate|location    |cost              |\n",
      "+---------------+----+------------+------------------+\n",
      "|Punjab Grill   |4.9 |Whitefield  |434.05749032614705|\n",
      "|Punjab Grill   |4.9 |Malleshwaram|354.86531986531986|\n",
      "|Punjab Grill   |4.9 |Malleshwaram|354.86531986531986|\n",
      "|Barbeque Nation|4.8 |JP Nagar    |429.76506639427987|\n",
      "|The Black Pearl|4.8 |Marathahalli|419.59418534221686|\n",
      "+---------------+----+------------+------------------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from pyspark.sql.functions import array_contains\n",
    "\n",
    "input_cuisine = \"North Indian\"\n",
    "\n",
    "filtered_recommendations = df.filter(array_contains(col(\"cuisines\"), input_cuisine)) \\\n",
    "    .select(\"name\", \"rate\", \"location\", \"cost\") \\\n",
    "    .orderBy(col(\"rate\").desc())\n",
    "filtered_recommendations.show(5, truncate=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------------+--------------------+------------+----------+----+--------------------+-----+--------+-----------+-------+\n",
      "|          location|                name|online_order|book_table|rate|            cuisines| cost|    type|location_id|name_id|\n",
      "+------------------+--------------------+------------+----------+----+--------------------+-----+--------+-----------+-------+\n",
      "|Kumaraswamy Layout|            Goa 0 Km|         Yes|       Yes| 3.6|[Goan,  Seafood, ...|800.0|Delivery|       43.0| 6946.0|\n",
      "|         Jayanagar|Namma Brahmin's Idli|         Yes|        No| 3.6|      [South Indian]|100.0|Delivery|        9.0| 4725.0|\n",
      "|      Basavanagudi|           Cane-O-La|         Yes|        No| 3.8|            [Juices]|100.0|Delivery|       18.0| 6560.0|\n",
      "|      Banashankari|  Sai Super Sandwich|         Yes|        No|3.65|[Sandwich,  Bever...|200.0|Desserts|       13.0| 2476.0|\n",
      "|      Banashankari|         Udupi Ruchi|         Yes|        No| 3.9|[South Indian,  N...|200.0|Dine-out|       13.0|  384.0|\n",
      "+------------------+--------------------+------------+----------+----+--------------------+-----+--------+-----------+-------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.show(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RMSE (Root Mean Squared Error): 82.46556657707407\n",
      "MAE (Mean Absolute Error): 37.9103018483598\n",
      "R² (R-Squared): 0.792857984073061\n",
      "+-----+------------------+\n",
      "|label|        prediction|\n",
      "+-----+------------------+\n",
      "|650.0| 716.7676915185725|\n",
      "|900.0| 876.4686256873098|\n",
      "|900.0| 879.4595367570539|\n",
      "|400.0| 383.4344299411883|\n",
      "|250.0|219.71118509365186|\n",
      "|300.0|247.74801859830143|\n",
      "|400.0|507.34090736970415|\n",
      "|600.0|  615.995400806944|\n",
      "|750.0| 738.0618334994151|\n",
      "|750.0| 744.0422368322457|\n",
      "|750.0| 749.0591284188696|\n",
      "|750.0| 741.7705378421074|\n",
      "|750.0|  767.245555506571|\n",
      "|500.0| 494.0198755922897|\n",
      "|500.0| 383.3057619043059|\n",
      "|400.0|415.73740038233785|\n",
      "|500.0|501.24626079846104|\n",
      "|400.0|398.45629984210103|\n",
      "|750.0| 743.9556520398469|\n",
      "|600.0| 602.9947059515791|\n",
      "+-----+------------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler\n",
    "from pyspark.ml.regression import LinearRegression\n",
    "from pyspark.ml import Pipeline\n",
    "from pyspark.sql.functions import col, concat_ws\n",
    "from pyspark.ml.evaluation import RegressionEvaluator\n",
    "from pyspark.ml.regression import LinearRegression\n",
    "\n",
    "df = df.withColumn(\"cuisines_str\", concat_ws(\",\", col(\"cuisines\"))).drop(\"cuisines\")\n",
    "\n",
    "categorical_columns = [\"name\", \"online_order\", \"book_table\", \"cuisines_str\", \"type\", \"location\"]\n",
    "\n",
    "indexers = [StringIndexer(inputCol=col, outputCol=col + \"_index\") for col in categorical_columns]\n",
    "encoders = [OneHotEncoder(inputCol=col + \"_index\", outputCol=col + \"_vec\") for col in categorical_columns]\n",
    "\n",
    "feature_columns = [col + \"_vec\" for col in categorical_columns] + [col for col in df.columns if col not in categorical_columns + [\"cost\"]]\n",
    "assembler = VectorAssembler(inputCols=feature_columns, outputCol=\"features\")\n",
    "\n",
    "pipeline = Pipeline(stages=indexers + encoders + [assembler])\n",
    "\n",
    "processed_data = pipeline.fit(df).transform(df)\n",
    "\n",
    "final_data = processed_data.select(\"features\", col(\"cost\").alias(\"label\"))\n",
    "\n",
    "train_data, test_data = final_data.randomSplit([0.8, 0.2], seed=42)\n",
    "\n",
    "lr = LinearRegression(featuresCol=\"features\", labelCol=\"label\")\n",
    "model = lr.fit(train_data)\n",
    "\n",
    "predictions = model.transform(test_data)\n",
    "\n",
    "evaluator_rmse = RegressionEvaluator(labelCol=\"label\", predictionCol=\"prediction\", metricName=\"rmse\")\n",
    "evaluator_mae = RegressionEvaluator(labelCol=\"label\", predictionCol=\"prediction\", metricName=\"mae\")\n",
    "evaluator_r2 = RegressionEvaluator(labelCol=\"label\", predictionCol=\"prediction\", metricName=\"r2\")\n",
    "\n",
    "rmse = evaluator_rmse.evaluate(predictions)\n",
    "print(f\"RMSE (Root Mean Squared Error): {rmse}\")\n",
    "\n",
    "mae = evaluator_mae.evaluate(predictions)\n",
    "print(f\"MAE (Mean Absolute Error): {mae}\")\n",
    "\n",
    "r2 = evaluator_r2.evaluate(predictions)\n",
    "print(f\"R² (R-Squared): {r2}\")\n",
    "predictions.select(\"label\", \"prediction\").show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_pandas = df.toPandas()\n",
    "df_pandas.to_csv(\"final_output.csv\", index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# new_data = spark.createDataFrame([\n",
    "#     (\"Banashankari\", \"New Cafe\", \"Yes\", \"No\", 4.2, 300.0, \"Cafe,Italian\", \"Delivery\", 13, 7859),\n",
    "#     (\"Basavanagudi\", \"Another Restaurant\", \"No\", \"Yes\", 3.8, 500.0, \"North Indian\", \"Dine-out\", 18, 3489)\n",
    "# ], [\"location\", \"name\", \"online_order\", \"book_table\", \"rate\", \"cost\", \"cuisines_str\", \"type\", \"location_id\", \"name_id\"])\n",
    "\n",
    "\n",
    "\n",
    "# # processed_new_data = pipeline.fit(df).transform(new_data)\n",
    "\n",
    "# # predictions_new = model.transform(processed_new_data)\n",
    "\n",
    "# # predictions_new.select(\"name\", \"location\", \"prediction\").show()\n",
    "\n",
    "\n",
    "# processed_new_data = pipeline.fit(df).transform(df.loc[:2,:])\n",
    "\n",
    "# predictions_new = model.transform(processed_new_data)\n",
    "\n",
    "# predictions_new.select(\"name\", \"location\", \"prediction\").show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# print(\"Schema of processed_new_data:\")\n",
    "# processed_new_data.printSchema()\n",
    "\n",
    "# print(\"Schema of predictions_new:\")\n",
    "# predictions_new.printSchema()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
