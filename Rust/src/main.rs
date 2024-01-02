use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn count_lines(path: &str) -> io::Result<(usize, String)> {
    let file = File::open(path).unwrap();
    let reader = io::BufReader::new(file);
    let basename = Path::new(path)
        .file_name()
        .unwrap_or_default()
        .to_string_lossy()
        .into();

    let count = reader
        .lines()
        .filter_map(|line| line.ok())
        .filter(
            |line|
            !line.trim().is_empty()
            && !line.trim().starts_with("#")
            && !line.trim().starts_with("'''")
            && !line.trim().starts_with("\"\"\"")
            && !line.trim().starts_with("--")
            && !line.trim().starts_with("//")
            && !line.trim().starts_with("/*")
        )
        .count();

    Ok((count, basename))
}


fn count_multiple(paths: &[&str]) -> (io::Result<usize>, String) {
    let mut total = 0;
    let mut basenames = Vec::new();

    for path in paths {
        let (count, basename) = count_lines(path).unwrap_or((0, String::new()));
        total += count;
        basenames.push(basename);
    }

    (Ok(total), basenames.join(", "))
}


fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: \n");
        eprintln!("     Single File: {} <file_path>\n", args[0]);
        eprintln!("     Multiple Files (sum): {} <file_path1> <file_path2>\n", args[0]);
        std::process::exit(1);
    }

    let file_paths: Vec<&str> = args[1..]
        .iter()
        .map(|s| s.as_str())
        .collect();

    if file_paths.len() == 1 {
        match count_lines(&file_paths[0]) {
            Ok((count, basename)) => println!("Lines of Code in {}: {}", basename, count),
            Err(err) => eprintln!("Error: {}", err),
        }
    } else if file_paths.len() >= 2 {
        let (count, basenames) = count_multiple(&file_paths);
        match count {
            Ok(total) => println!("Lines of Code in {}: {}", basenames, total),
            Err(err) => eprintln!("Error: {}", err),
        }
    }
}
