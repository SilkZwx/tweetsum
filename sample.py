from tweet_sum_processor import TweetSumProcessor

def main():
    TWCS_FILE_PATH = 'archive/twcs/twcs.csv'
    TWEET_SUMM_FILE_PATH = 'tweet_sum_data_files/final_test_tweetsum.jsonl'
    processor = TweetSumProcessor(TWCS_FILE_PATH)
    with open(TWEET_SUMM_FILE_PATH) as f:
        dialog_with_summaries = processor.get_dialog_with_summaries(f.readlines())
        for dialog_with_summary in dialog_with_summaries:
            json_format = dialog_with_summary.get_json()
            string_format = str(dialog_with_summary)
            print(json_format)
            print(string_format)
            input('wait')

if __name__ == "__main__":
    main()